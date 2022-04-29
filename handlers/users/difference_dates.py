from datetime import datetime
from dateutil.relativedelta import relativedelta
import pymorphy2
from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.builtin import Command
from loader import dp
from aiogram.dispatcher import FSMContext
from states import States_difference_date


@dp.message_handler(Command("difference_between_dates"))
async def start_detect_years(message: types.Message):
    await States_difference_date.data_1.set()
    await message.answer("Напишите первую дату. Пример: 03.09.1994")

@dp.message_handler(filters.Regexp( r'^(0?[1-9]|[12][0-9]|3[01]).(0?[1-9]|1[012]).((15|16|17|18|19|20)\d\d)$' ), state=States_difference_date.data_1)
async def detect_years(message: types.Message, state: FSMContext):
    data_1 = datetime(
        day=int(message.text.split('.')[0]),
        month=int(message.text.split('.')[1]),
        year=int(message.text.split('.')[2])
    )
    await state.update_data(data_1=data_1, data_1_message=message.text)
    await States_difference_date.next()
    await message.answer('Введите следующую дату')

@dp.message_handler(filters.Regexp( r'^(0?[1-9]|[12][0-9]|3[01]).(0?[1-9]|1[012]).((15|16|17|18|19|20)\d\d)$' ), state=States_difference_date.data_2)
async def detect_years(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data_1 = data['data_1']

        data_2 = datetime(
            day=int(message.text.split('.')[0]),
            month=int(message.text.split('.')[1]),
            year=int(message.text.split('.')[2])
        )

        difference = relativedelta(data_2, data_1)

        def morph(word, number):
            word = pymorphy2.MorphAnalyzer().parse(word)[0].make_agree_with_number(number).word
            if word == 'годов'.lower():
                word = 'лет'
            return word

        await message.answer(f'Разница между датой <b>{data["data_1_message"]}</b> и <b>{message.text}</b> составляет:\n'
                             f'<b>{abs(difference.years)} {morph("год", difference.years)}, '
                             f'{abs(difference.months)} {morph("месяц", difference.months)}, '
                             f'{abs(difference.days)} {morph("день", difference.days)}</b>')

        await state.finish()
        await state.set_state(States_difference_date.data_1)
