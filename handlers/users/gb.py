from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from filters import IsDigit
from keyboards.inline.data_converter import callback
from loader import dp
from aiogram.dispatcher import FSMContext
from keyboards.inline import data_converter_keyboard
from states import DataConverterState

@dp.message_handler(Command('data_converter'))
async def discount(message: types.Message, state: FSMContext):
    await message.answer('выберите величину', reply_markup=data_converter_keyboard)
    await state.set_state(DataConverterState.convert_from.state)

@dp.callback_query_handler(callback.filter(), state=DataConverterState.convert_from)
async def get_from(call: CallbackQuery,  callback_data: dict, state: FSMContext):
    await call.message.delete()
    message = await call.message.answer(f"<b>{callback_data.get('name')}</b> ➡ ")
    message_keyboards = await call.message.answer('выберите величину', reply_markup=data_converter_keyboard)
    await state.update_data(name1=callback_data.get('name'), v1 = callback_data.get('value'), message=message, keyboards=message_keyboards)
    await DataConverterState.next()
@dp.callback_query_handler(callback.filter(), state=DataConverterState.convert_to)
async def get_next_value(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(name2=callback_data.get('value'), v2 = callback_data.get('value'),)
    async with state.proxy() as data:
        await data['keyboards'].delete()
        await data['message'].edit_text(f"<b>{data['name1']}</b> ➡ <b>{callback_data.get('name')}</b> \n \n"
                                        f"<i>Отправьте значение</i>")
    await DataConverterState.next()


@dp.message_handler(IsDigit(), state=DataConverterState.value)
async def get_data(message: types.Message, state: FSMContext):
    def convert(convert_from, convert_to, value):
        return value * 1024**(convert_from - convert_to)

    async with state.proxy() as data:
        await message.answer(f'Результат: <b>{convert(int(data["v1"]), int(data["v2"]), int(message.text))}</b>')
    await state.finish()



