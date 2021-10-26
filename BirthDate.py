import datetime

list_of_birth = [["Fedor", datetime.datetime(1998, month=10, day=20)],
                 ["Bogdan", datetime.datetime(1998, month=10, day=12)],
                 ["test", datetime.datetime(1998, month=10, day=26)],
                 ["Max", datetime.datetime(1998, month=5, day=3)],
                 ["Nikita Lameev", datetime.datetime(1999, month=1, day=14)]

                 ]
today = datetime.datetime.now()


def get_message_birth():
    message_string = ""
    for dates in list_of_birth:
        timestamp = (dates[1].month - today.month) + (dates[1].day - today.day)
        if timestamp == 0:
            message_string += f"\nСегодня день рождения у {dates[0]}!!!\nЕму {today.year - dates[1].year}!"
        elif timestamp > 0:
            message_string += f"{dates[0]} через {timestamp} дней ({dates[1].month}.{dates[1].day}) \n"
        elif timestamp in range(-14, 0):
            message_string += f"{dates[0]} был {timestamp * (-1)} дней назад ({dates[1].month}.{dates[1].day}) \n"
    return message_string
