from datetime import datetime
from dateutil.relativedelta import relativedelta
import pymorphy2
from aiogram import types
from aiogram.dispatcher import filters, FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from states import year


@dp.message_handler(Command("detect_years"), state="*")
async def start_detect_years(message: types.Message, state: FSMContext):
    await state.finish()
    await year.set()
    await message.answer("Напишите полную дату рождения. Пример: 03.09.1994", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(filters.Regexp(r'^(0?[1-9]|[12][0-9]|3[01]).(0?[1-9]|1[012]).((17|18|19|20)\d\d)$'), state=year)
async def detect_years(message: types.Message, state: FSMContext):
    birthday_date = datetime(
        day=int(message.text.split(".")[0]),
        month=int(message.text.split(".")[1]),
        year=int(message.text.split(".")[2])
    )

    time_now = datetime.now()
    since_the_birthday = relativedelta(time_now, birthday_date)
    if time_now.month > birthday_date.month:
        next_birthday_date = birthday_date.replace(year=time_now.year + 1)
    else:
        next_birthday_date = birthday_date.replace(year=time_now.year)

    if birthday_date.month <= time_now.month:
        if birthday_date.day >= time_now.day:
            pass
        else:
            next_birthday_date = birthday_date.replace(year=time_now.year + 1)

    time_to_next_birthday = relativedelta(next_birthday_date, time_now)

    def morph(word, number):
        word = pymorphy2.MorphAnalyzer().parse(word)[0].make_agree_with_number(number).word
        if word == 'годов'.lower():
            word = 'лет'
        return word

    def week():
        weeks = {0: 'Понедельник', 1: 'Вторник', 2: "Среду", 3: "Четверг", 4: "Пятницу", 5: "Субботу", 6: "Воскресенье"}

        week = birthday_date.replace(year=time_now.year).weekday()
        if since_the_birthday.hours != 0 or since_the_birthday.minutes != 0:
            if week == 6:
                week = 0
            else:
                week += 1
        return weeks[week]

    def month():
        months = {1: 'Января', 2: 'Февраля', 3: 'Марта', 4: 'Апреля', 5: 'Мая', 6: 'Июня', 7: "Июля",
                  8: 'Августа', 9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}

        return months[birthday_date.month]

    result = f"Возраст<b>: {since_the_birthday.years} {morph('год', since_the_birthday.years)}, " \
             f"{since_the_birthday.months} {morph('месяц', since_the_birthday.months)}, " \
             f"{since_the_birthday.days} {morph('день', since_the_birthday.days)}</b>\n" \
             f"До следующего дня рождения:<b> {time_to_next_birthday.months} {morph('месяц', time_to_next_birthday.months)}, " \
             f" {time_to_next_birthday.days} {morph('день', time_to_next_birthday.days)}, " \
             f" {time_to_next_birthday.hours} {morph('час', time_to_next_birthday.hours)}</b> \n" \
             f"🎉 следующий день рождения <b>{birthday_date.day} {month()} в {week()}</b>"

    await message.answer(result)
    await state.finish()
    await state.set_state(year)
