import os

import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def conn():
    DATABASE_URL = os.environ['DATABASE_URL']

    try:
        connection = psycopg2.connect(DATABASE_URL, sslmode='require')
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
