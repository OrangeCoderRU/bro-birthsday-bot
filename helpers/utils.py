import datetime
import time

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


def validate_date(date):
    try:
        value = time.strptime(date, "%d %B %Y")
        return value
    except:
        return "Error"


def validate_all_input(input: str):
    if input.count('\n') != 1:
        return "Error"
    else:
        return "Ok"