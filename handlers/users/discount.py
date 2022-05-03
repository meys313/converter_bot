from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from filters import IsDigit, DiscountFilter
from loader import dp
from aiogram.dispatcher import FSMContext
from states import DiscountState




@dp.message_handler(Command('discount'), state="*")
async def discount(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('введите первоночальную цену', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(DiscountState.price)

@dp.message_handler(IsDigit(), state=DiscountState.price)
async def get_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer('введите скидку')
    await DiscountState.next()
@dp.message_handler(IsDigit(), DiscountFilter(), state= DiscountState.discount)
async def get_discount(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        price = int(data["price"])
        discount = int(message.text)

        discount_result = (discount*price) / 100
        price_result = price - discount_result

        await message.answer(f'Цена: <b>{data["price"]}</b>, скидка: <b>{message.text}</b> \n'
                             f'Вы сэкономите: <b>{discount_result}</b>, итоговая цена: <b>{price_result}</b>')

    await state.finish()
    await state.set_state(DiscountState.price)

@dp.message_handler(state= DiscountState.all_states)
async def incorrect_data(message: types.Message):
    await message.answer('Похоже, что введены некорректные данные \n'
                         '(Скидка: положительное число от нуля до ста)')

