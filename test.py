from datetime import date, datetime, timedelta
import calendar

today = datetime.today()

birthday = datetime(day=5, month=11, year=today.year)

next_birthday_days = birthday - today

print(next_birthday_days)
hour = int(str(next_birthday_days).split(',')[1].split(':')[0])
minute = int(str(next_birthday_days).split(',')[1].split(':')[1])

birthday_month = (today + timedelta(days=next_birthday_days.days)).month


def detect_next_birthday():
    key = {}
    summ = 197
    if hour != 0 and minute != 0:
        summ +=1
    month = 0
    day = 0
    for m in range(today.month, birthday_month + 1):
        key.update({m: calendar.monthrange(2022, m)[1]})

    for key, value in key.items():
        if summ > value:
            summ = summ - value
            month +=1
    day = summ


    print(f"до дня рождения осталось месяцев: {month} и дней: {day}")

detect_next_birthday()


