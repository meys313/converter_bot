import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageNotModified

from keyboards.inline.default_inline_calculator import default_calculator, callback

from loader import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class Form(StatesGroup):
    number = State()

@dp.message_handler(Command('default_calculator'))
async def default_calculator_handlers(message: types.Message, state: FSMContext ):
    await message.answer('Простой калькулятор: ', reply_markup=default_calculator)
    await Form.number.set()

@dp.callback_query_handler(callback.filter(), state=Form.number)
async def default_calculator_callback(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    if callback_data.get('value') != '=':
        if not await state.get_data():
            await state.update_data(my_list=[callback_data.get('value'), ])
            await call.message.edit_text(f"Простой калькулятор: {callback_data.get('value')}",
                                         reply_markup=default_calculator)
        else:
            async with state.proxy() as data:
                data['my_list'].append(callback_data.get('value'))
                await call.message.edit_text(f"Простой калькулятор: {''.join(data['my_list'])}", reply_markup=default_calculator)
    else:
        async with state.proxy() as data:
            try:
                await call.message.edit_text(f'Простой калькулятор: {eval("".join(data.pop("my_list")))}', reply_markup=default_calculator)
                await state.reset_data()
            except MessageNotModified:
                pass
            except SyntaxError:
                await call.message.edit_text(f'Простой калькулятор: Некорректные данные, попробуйте снова',
                                             reply_markup=default_calculator)








