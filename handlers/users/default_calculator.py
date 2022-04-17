from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.builtin import Command
from loader import dp, bot
from aiogram.dispatcher import FSMContext

from keyboards.default.default_calculator import calculator
from states.keyboard import StatesKeyboard
from filters import MyFilter


@dp.message_handler(Command('test'))
async def test(message: types.Message):
    await message.answer('Простой калькулятор', reply_markup=calculator)
    message = await message.answer('this is text')
    await sleep(3)
    await message.edit_text(text='this is edit text')




@dp.message_handler(Command('standart'))
async def state_start(message: types.Message, state: FSMContext):
    await StatesKeyboard.number.set()
    await bot.send_message(chat_id='5065186765', text='Калькулятор запущен', reply_markup=calculator)
    message_io = await message.answer('Вывод: ')


    @dp.message_handler(MyFilter(), state=StatesKeyboard.number, content_types=types.ContentTypes.TEXT)
    async def process_state(message: types.Message, state: FSMContext):
        if not await state.get_data():
            await state.update_data(my_list=[message.text, ])
        else:
            async with state.proxy() as data:
                data['my_list'].append(message.text)
        data = await state.get_data('my_list')
        await message_io.edit_text(text=f"Вывод: {''.join(data.get('my_list'))}")
        await message.chat.delete_message(message_id=message.message_id)


        @dp.message_handler(filters.Regexp(r"^[.=]$"), state=StatesKeyboard.number)
        async def result( message: types.message, state: FSMContext):

            async with state.proxy() as data:

                await message_io.edit_text(text=f'Результат = {eval("".join(data.get("my_list")))}')
                await message.chat.delete_message(message_id=message.message_id)
                await state.reset_data()





