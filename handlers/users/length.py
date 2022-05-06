from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from filters import IsDigit
from keyboards.inline.weight import callback
from loader import dp
from aiogram.dispatcher import FSMContext
from keyboards.inline import length_keyboard
from states import LengthStates

@dp.message_handler(Command('length'), state = "*")
async def discount(message: types.Message, state: FSMContext):
    await message.answer('выберите величину из которой вы хотите перевести', reply_markup=length_keyboard)
    await state.finish()
    await state.set_state(LengthStates.convert_from.state)

@dp.callback_query_handler(callback.filter(), state=LengthStates.convert_from)
async def get_from(call: CallbackQuery,  callback_data: dict, state: FSMContext):
    await call.message.delete()
    message = await call.message.answer(f"<b>{callback_data.get('name')}</b> ➡ ")
    message_keyboards = await call.message.answer('выберите величину в которую вы хотите перевести', reply_markup=length_keyboard)
    await state.update_data(name1=callback_data.get('name'), v1=callback_data.get('value'), message=message, keyboards=message_keyboards)
    await LengthStates.next()
@dp.callback_query_handler(callback.filter(), state=LengthStates.convert_to)
async def get_to(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(name2=callback_data.get('name'), v2=callback_data.get('value'),)
    async with state.proxy() as data:
        await data['keyboards'].delete()
        await data['message'].edit_text(f"<b>{data['name1']}</b> ➡ <b>{callback_data.get('name')}</b> \n \n"
                                        f"<i>Отправьте значение</i>")
    await LengthStates.next()


@dp.message_handler(IsDigit(), state=LengthStates.value)
async def get_value(message: types.Message, state: FSMContext):
    def convert(convert_from, convert_to, value):
        return value * 10**(convert_from - convert_to)

    async with state.proxy() as data:
        await message.answer(f'В {message.text} {data["name1"]}: \n'
                             f'<b>{convert(int(data["v1"]), int(data["v2"]), int(message.text))}</b> {data["name2"]}')
    await state.finish()

@dp.message_handler(state=LengthStates.value)
async def incorrect_data(message: types.Message):
    await message.answer('значение может быть только числом. Попробуйте снова')