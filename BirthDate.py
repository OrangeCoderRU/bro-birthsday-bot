import datetime

list_of_birth = [
    ["Федор", datetime.datetime(1998, month=10, day=20)],
    ["Богдан", datetime.datetime(1998, month=10, day=12)],
    ["Артур", datetime.datetime(1998, month=9, day=10)],
    ["Максим", datetime.datetime(1998, month=5, day=3)],
    ["Никита Ламеев", datetime.datetime(1999, month=1, day=14)],
    ["Руслан", datetime.datetime(1998, month=7, day=31)],
    ["Никита Горбачев", datetime.datetime(2000, month=7, day=11)]
]
today = datetime.datetime.now()


def to_up_date(list_birth):
    return today.month - list_birth[1].month, today.day - list_birth[1].day


def get_message_birth():
    message_string = ""
    for dates in list_of_birth:
        # timestamp = (dates[1].month - today.month) + (dates[1].day - today.day)
        if today.month == dates[1].month:
            timestamp = dates[1].day - today.day
            if timestamp == 0:
                message_string += f"\nСегодня день рождения у {dates[0]}!!!\nЕму {today.year - dates[1].year}!"
            elif timestamp in range(1, 14):
                message_string += f"{dates[0]} через {timestamp} дней ({dates[1].month}.{dates[1].day}) \n"
            elif timestamp in range(-14, 0):
                message_string += f"{dates[0]} был {timestamp * (-1)} дней назад ({dates[1].month}.{dates[1].day}) \n"
    return message_string


def get_all_birth():
    message_string = "Все др ваших братишек:\n"
    i = 0
    for dates in sorted(list_of_birth, key=to_up_date, reverse=True):
        if i == 0:
            message_string += f"\nБлижайший др - {dates[0]} - {dates[1].day}.{dates[1].month}.{dates[1].year}\n\n"
        else:
            message_string += f"{dates[0]} - {dates[1].day}.{dates[1].month}.{dates[1].year}\n"
        i += 1

    return message_string
