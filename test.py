import datetime
from dateutil.relativedelta import relativedelta


def get_time_since_the_birthday(birthday_date):
    time_now = datetime.datetime.now()
    since_the_birthday = relativedelta(time_now, birthday_date)

    print(f"со дня рождения прошло: {since_the_birthday}")

def get_time_to_next_birhday(birthday_date):
    time_now = datetime.datetime.now()
    next_birthday_date = birthday_date.replace(year=time_now.year +1)
    time_to_next_birthday = relativedelta(next_birthday_date, time_now)

    print(f"до следующего др: { time_to_next_birthday}")



birthday_dates = [2020, 3, 13]
birthday_date_time = datetime.datetime(*birthday_dates)

print(birthday_date_time)
get_time_since_the_birthday(birthday_date_time)
print(birthday_date_time.replace(year=2022).weekday())
get_time_to_next_birhday(birthday_date_time)


