from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageNotModified
from loader import dp
from aiogram.dispatcher import FSMContext

from keyboards.inline.inline_calculator import default_calculator, callback
from states.keyboard import StatesKeyboard


@dp.message_handler(Command('default_calculator'))
async def default_calculator_handlers(message: types.Message):
    await message.answer('🧮 Простой калькулятор: ', reply_markup=default_calculator)
    await StatesKeyboard.number.set()

@dp.callback_query_handler(callback.filter(), state=StatesKeyboard.number)
async def default_calculator_callback(call: CallbackQuery, callback_data: dict, state: FSMContext):

    if callback_data.get('value') == 'clear':
        await state.reset_data()
        await call.message.edit_text('🧮 Простой калькулятор: ', reply_markup=default_calculator)

    elif callback_data.get('value') == 'delete':
        async with state.proxy() as data:

            try:
                data['my_list'].remove(data['my_list'][-1])
                await call.message.edit_text(f"🧮 Простой калькулятор: {''.join(data['my_list'])}",
                                             reply_markup=default_calculator)
            except:
                await call.message.edit_text(f"🧮 Простой калькулятор: ",
                                             reply_markup=default_calculator)



    elif callback_data.get('value') != '=':
        if not await state.get_data():
            await state.update_data(my_list=[callback_data.get('value'), ])
            await call.message.edit_text(f"🧮 Простой калькулятор: {callback_data.get('value')}",
                                         reply_markup=default_calculator)
        else:
            async with state.proxy() as data:
                data['my_list'].append(callback_data.get('value'))
                await call.message.edit_text(f"🧮 Простой калькулятор: {''.join(data['my_list'])}", reply_markup=default_calculator)

    else:
        async with state.proxy() as data:
            try:
                await call.message.edit_text(f'🧮 Простой калькулятор: {eval("".join(data.pop("my_list")))}', reply_markup=default_calculator)
                await state.reset_data()
            except MessageNotModified:
                pass
            except SyntaxError:
                await call.message.edit_text(f'🧮 Простой калькулятор: Некорректные данные, попробуйте снова',
                                             reply_markup=default_calculator)








