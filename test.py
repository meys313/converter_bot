
def get_time(type,value):

    from_type_to_seconds = {
        'minutes': value * 60,
        'hours': (value * 60) * 60,
        'days': (value * 24) * 3600,
        'weeks': 3600 * ((value * 7) * 24)
    }
    get_seconds = from_type_to_seconds[type]
    seconds = get_seconds
    minutes = get_seconds / 60
    hours = minutes / 60
    days = hours / 24
    weeks = days / 7

    return {'s': seconds, 'm': minutes, 'h': hours, 'd': days, 'w': weeks}


print(get_time('weeks', 5)['s'])
