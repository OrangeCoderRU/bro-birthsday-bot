import datetime

today = datetime.datetime.now()


def to_up_date(list_birth):
    return today.month - list_birth[1].tm_mon, today.day - list_birth[1].tm_mday


def sort_actual(check_birth):
    return check_birth[0]


def map_month(month_num):
    list_month = [
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря"
    ]
    return list_month[month_num - 1]
