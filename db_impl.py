import os

import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# try:
#     # Подключение к существующей базе данных
#     connection = psycopg2.connect(
#         database="dfo9956jt4pj6u",
#         user="qovhiaqjytdesz",
#         password="c7a64d744fa9a96dec568a04112ad091130490f66fd6ad80c6977be88a03c41a",
#         host="ec2-54-154-101-45.eu-west-1.compute.amazonaws.com",
#         port="5432")
#     connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#     cursor = connection.cursor()
#     # select_query = "SELECT * FROM data"
#     # cursor.execute(select_query)
#     # print(cursor.fetchall())
# except (Exception, Error) as error:
#     print("Ошибка при работе с PostgreSQL", error)
#

# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("Соединение с PostgreSQL закрыто")

def conn():
    DATABASE_URL = os.environ['DATABASE_URL']

    try:
        connection = psycopg2.connect(DATABASE_URL, sslmode='require')
        # connection = psycopg2.connect(
        #     database="dfo9956jt4pj6u",
        #     user="qovhiaqjytdesz",
        #     password="c7a64d744fa9a96dec568a04112ad091130490f66fd6ad80c6977be88a03c41a",
        #     host="ec2-54-154-101-45.eu-west-1.compute.amazonaws.com",
        #     port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
    except (Exception, Error) as error:
        cursor = None
        print("Ошибка при работе с PostgreSQL", error)
        raise Error

    return cursor, connection


def close_conn(cursor, connection):
    cursor.close()
    connection.close()
    print("Соединение с PostgreSQL закрыто")


def get_members_for_chat(chat_id):
    query = f"SELECT snapshot FROM DATA WHERE chat_id LIKE '{chat_id}'"
    cursor = conn()
    cursor[0].execute(query)
    snapshot = cursor[0].fetchall()
    cursor[0].close()
    close_conn(cursor[0], cursor[1])
    return snapshot


def set_members_for_chat(chat_id, snapshot):
    query = f"INSERT INTO DATA (snapshot, chat_id) VALUES('{snapshot}', {chat_id})"
    cursor = conn()
    cursor[0].execute(query)
    cursor[0].close()
    close_conn(cursor[0], cursor[1])


# set_members_for_chat(5557)
# set_members_for_chat(5557)
# set_members_for_chat(5558)

# get_members_for_chat(5557)
