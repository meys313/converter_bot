from datetime import datetime
import calendar
import pymorphy2
from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from loader import dp, bot
from aiogram.dispatcher import FSMContext

from keyboards.default.default_calculator import calculator
from keyboards.inline.clear_btn import inline_btn, callbackButton
from states.years import states_years
from filters import MyFilter

@dp.message_handler(Command("detect_years"))
async def start_detect_years(message: types.Message):
    await states_years.set()
    await message.answer("Напишите полную дату рождения. Пример: 03.09.1994")

# хэндлер на текст формата 21.04.2020 (год в пределах 1700, 1800, 1900, 2000) с установленным состоянием states_years
@dp.message_handler(filters.Regexp( r'^(0?[1-9]|[12][0-9]|3[01]).(0?[1-9]|1[012]).((17|18|19|20)\d\d)$' ), state=states_years)
async def detect_years(message: types.Message, state: FSMContext):
    birthday = datetime(
        day=int(message.text.split(".")[0]),
        month=int(message.text.split(".")[1]),
        year=int(message.text.split(".")[2])
    ) # формирует дату рождения из данных, отправленных пользователем

    today = message.date.today() # сегодняшнее число

    day = abs(today.day - birthday.day)
    month = today.month - birthday.month

    if month < 0:
        month = 12 - abs(month)
    if today.day < birthday.day:
        day = calendar.monthrange(today.year, today.month - 1)[1] - day
        if month != 0:
            month -= 1
    year = today.year - birthday.year
    if today.month < birthday.month or today.month == birthday.month and today.day < birthday.day:
        year -= 1

    def morph(word, number):
        word = pymorphy2.MorphAnalyzer().parse(word)[0].make_agree_with_number(number).word
        if word == 'годов'.lower():
            word = 'лет'
        return word

    result = f"Возраст {year} {morph('год', year)}, {month} {morph('месяц', month)}, {day} {morph('день', day)} \n" \
             f"Следующий день рождения: "

    await message.answer(result)