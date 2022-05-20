import ast
import operator as op
from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from loader import dp, bot
from aiogram.dispatcher import FSMContext

from keyboards.default.default_calculator import calculator
from keyboards.inline.clear_btn import inline_btn, callbackButton
from states.keyboard import StatesKeyboard
from filters import MyFilter


# хендлер на команду /default_calculator
@dp.message_handler(Command('default_calculator'), state="*")
async def state_start(message: types.Message, state: FSMContext):
    await state.finish()
    await StatesKeyboard.number.set()
    await StatesKeyboard.message_id.set()
    await bot.send_message(chat_id=message.chat.id, text='Калькулятор запущен.\n\n'
                                                         '❗<i> если нажимать на кнопки слишком быстро, бот может не успевать обрабатывать сообщения, вследсвтии чего может принимать данные некорретно ❗</i>\n\n'
                                                         'Вы также можете ввести данные от руки <u> 248 + 20 </u> затем отправив <b>=</b> отдельным сообщением для получения результата \n\n'
                                                         ' /cancel - выйти', reply_markup=calculator)
    message_io = await message.answer('📝 Вывод: ', reply_markup=inline_btn)
    await state.update_data(message_id=message_io.message_id)


@dp.message_handler(MyFilter(), state=StatesKeyboard.all_states, content_types=types.ContentTypes.TEXT)
async def process_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if not data.get('my_list'):
            data.update(my_list=[message.text, ])
        else:
            data['my_list'].append(message.text)

        await bot.edit_message_text(chat_id=message.chat.id, message_id=data['message_id'],
                                    text=f"Вывод: {''.join(data.get('my_list'))}", reply_markup=inline_btn)
        await message.chat.delete_message(message_id=message.message_id)


@dp.message_handler(filters.Regexp(r"^[.=]$"), state=StatesKeyboard.all_states)
async def result(message: types.message, state: FSMContext):
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
        try:
            result = eval_expr("".join(data.get("my_list")))
        except ZeroDivisionError:
            result = '<i>❗Упс, кажется ты пытаешься делить на ноль❗</i>'
        await bot.edit_message_text(chat_id=message.chat.id, message_id=data['message_id'],
                                    text=f'Результат = {result}', reply_markup=inline_btn)
        await message.chat.delete_message(message_id=message.message_id)
        data['my_list'].clear()


@dp.callback_query_handler(callbackButton.filter(), state=StatesKeyboard.all_states)
async def clear_button(call: CallbackQuery, callback_data: dict, state: FSMContext):
    async with state.proxy() as data:
        data['my_list'].clear()
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=data['message_id'],
                                text='Вывод: ', reply_markup=inline_btn)
