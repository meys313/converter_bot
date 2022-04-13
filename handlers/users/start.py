from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

class Form(StatesGroup):
    number = State()


@dp.message_handler(Command('start'), )
async def state_start(message: types.Message, state: FSMContext):
    await Form.number.set()
    await bot.send_message(chat_id='5065186765', text='Состояние установлено')


@dp.message_handler(filters.Regexp(r"^[0-9 .+*\/-]*$"), state=Form.number, content_types=types.ContentTypes.TEXT)
async def process_state(message: types.Message, state: FSMContext):

    if not await state.get_data():
        await state.update_data(my_list=[message.text, ])
    else:
        async with state.proxy() as data:
            data['my_list'].append(message.text)
            await bot.send_message(chat_id='5065186765', text=data.get('my_list'))


    @dp.message_handler(filters.Regexp(r"^[.=]$"), state=Form.number)
    async def result( message: types.message, state: FSMContext):
        async with state.proxy() as data:

            await bot.send_message(chat_id='5065186765', text=f'result = {eval("".join(data.get("my_list")))}')
            await state.reset_data()





