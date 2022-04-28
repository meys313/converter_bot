import datetime
from dateutil.relativedelta import relativedelta


def get_time_difference(date_time, date2_time):

    since_the_time = relativedelta(date2_time, date_time)

    print(f"Разница: {since_the_time}")





data1 = [1994, 9, 13]
data2 = [1995, 9, 13]
date_time = datetime.datetime(*data1)
date2_time = datetime.datetime(*data2)

get_time_difference(date_time, date2_time)

