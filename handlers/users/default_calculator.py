import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from keyboards.inline.default_inline_calculator import default_calculator, count, operator
from loader import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

text_message = 'простой калькулятор'

@dp.message_handler(Command('d'))
async def d(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='привет')

@dp.message_handler(Command('default_calculator'))
async def default_calculator_handlers(message: types.Message, state: FSMContext ):
    await message.answer(text_message, reply_markup=default_calculator)

    num = State()
    await num.set()

    await state.update_data(num=str())


@dp.callback_query_handler(count.filter())
async def default_calculator_callback(call: CallbackQuery, callback_data: dict, state: FSMContext):

    await call.answer()

    # async with state.proxy() as data:

    fsm_number = await state.get_data()
    number = callback_data.get('number')

    async with state.proxy() as data:
        data['num'] += number
        await call.message.edit_text(f"{text_message}: {data['num']}", reply_markup=default_calculator)

@dp.callback_query_handler(operator.filter())
async def operators(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()

    if callback_data['operator'] == '+':
        async with state.proxy() as data:
            result = int(data['num']) + 10
            await call.message.answer(str(result))

