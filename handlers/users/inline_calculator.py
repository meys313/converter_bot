import ast
import operator as op
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageNotModified

from filters import InlineClear, InlineDelete
from loader import dp
from aiogram.dispatcher import FSMContext

from keyboards.inline.inline_calculator import default_calculator, callback
from states.keyboard import StatesKeyboard


@dp.message_handler(Command('inline_calculator'), state="*")
async def default_calculator_handlers(message: types.Message, state: FSMContext):
    await message.answer(text='Калькулятор запущен.\n\n'
                        '❗<i> если нажимать на кнопки слишком быстро, бот может не успевать обрабатывать данные, вследсвтии чего может принимать данные некорретно ❗</i>\n\n')
    await message.answer('🧮 Простой калькулятор: ', reply_markup=default_calculator)
    await state.finish()
    await StatesKeyboard.number.set()


@dp.callback_query_handler(callback.filter(), InlineClear(), state=StatesKeyboard.number)
async def inline_clear(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await state.reset_data()
    try:
        await call.message.edit_text('🧮 Простой калькулятор: ', reply_markup=default_calculator)
    except MessageNotModified:
        pass


@dp.callback_query_handler(callback.filter(), InlineDelete(), state=StatesKeyboard.number)
async def inline_delete(call: CallbackQuery, callback_data: dict, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['my_list'].remove(data['my_list'][-1])
            await call.message.edit_text(f"🧮 Простой калькулятор: {''.join(data['my_list'])}",
                                         reply_markup=default_calculator)
        except IndexError:
            try:
                await call.message.edit_text(f"🧮 Простой калькулятор: ",
                                             reply_markup=default_calculator)
            except MessageNotModified:
                pass



@dp.callback_query_handler(callback.filter(), state=StatesKeyboard.number)
async def inline_calculator_callback(call: CallbackQuery, callback_data: dict, state: FSMContext):
    def eval_expr(expr):
        return eval_(ast.parse(expr, mode='eval').body)

    def eval_(node):

        operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
                     ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
                     ast.USub: op.neg}
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            return operators[type(node.op)](eval_(node.left), eval_(node.right))
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
            return operators[type(node.op)](eval_(node.operand))
        else:
            raise TypeError(node)

    async with state.proxy() as data:
        if callback_data.get('value') != '=':
            if not await state.get_data():
                data.update(my_list=[callback_data.get('value'), ])
            else:
                data['my_list'].append(callback_data.get('value'))
            await call.message.edit_text(f"🧮 Простой калькулятор: {''.join(data['my_list'])}", reply_markup=default_calculator)

        # если пришло =
        else:
            try:
                await call.message.edit_text(f'🧮 Простой калькулятор: {eval_expr("".join(data.pop("my_list")))}', reply_markup=default_calculator)
                await state.reset_data()
            except MessageNotModified:
                pass
            except ZeroDivisionError:
                await call.answer('Упс, кажется ты пытаешься делить на ноль')
                await call.message.edit_text(f'🧮 Простой калькулятор: ',
                                             reply_markup=default_calculator)
            except SyntaxError:
                await call.answer('Некорректные данные, попробуйте снова')
                await call.message.edit_text(f'🧮 Простой калькулятор: ',
                                             reply_markup=default_calculator)






