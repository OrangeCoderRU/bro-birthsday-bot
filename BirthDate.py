from utils import sort_actual, to_up_date, map_month
import datetime

list_of_birth = [
    ["Федор", datetime.datetime(1998, month=10, day=20)],
    ["Богдан", datetime.datetime(1998, month=10, day=12)],
    ["Артур", datetime.datetime(1998, month=9, day=10)],
    ["Максим", datetime.datetime(1998, month=5, day=3)],
    ["Никита Ламеев", datetime.datetime(1999, month=1, day=14)],
    ["Руслан", datetime.datetime(1998, month=7, day=31)],
    ["Никита Горбачев", datetime.datetime(2000, month=7, day=11)],
    # ["test user", datetime.datetime(2001, month=10, day=29)]
]
today = datetime.datetime.now()


def get_message_birth():
    message_string = ""
    check_birth_list = []
    for dates in list_of_birth:
        # timestamp = (dates[1].month - today.month) + (dates[1].day - today.day)
        if today.month == dates[1].month:
            timestamp = dates[1].day - today.day
            check_birth_list.append([timestamp, dates])

    for actual_birth in sorted(check_birth_list, key=sort_actual, reverse=True):
        if actual_birth[0] == 0:
            message_string += f"\nСегодня день рождения у {actual_birth[1][0]}!!!\nЕму {today.year - actual_birth[1][1].year}!\n\n"
        elif actual_birth[0] in range(1, 31):
            message_string += f"{actual_birth[1][0]} через {actual_birth[0]} дней ({actual_birth[1][1].day} {map_month(actual_birth[1][1].month)}) \n"
        elif actual_birth[0] in range(-31, 0):
            message_string += f"{actual_birth[1][0]} был {actual_birth[0] * (-1)} дней назад ({actual_birth[1][1].day} {map_month(actual_birth[1][1].month)})\n"
    return message_string


def get_all_birth():
    message_string = "Все др ваших братишек:\n"
    i = 0
    for dates in sorted(list_of_birth, key=to_up_date, reverse=True):
        if i == 0:
            message_string += f"\nБлижайший др:\n{dates[0]} - {dates[1].day} {map_month(dates[1].month)}\n\n"
        else:
            message_string += f"{dates[0]} - {dates[1].day} {map_month(dates[1].month)}\n"
        i += 1

    return message_string
