import os

import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from settings import DATABASE_URL


def conn():
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


def get_members_and_chats_id():
    query = f"SELECT snapshot, chat_id FROM DATA"
    cursor = conn()
    cursor[0].execute(query)
    data = cursor[0].fetchall()
    cursor[0].close()
    close_conn(cursor[0], cursor[1])
    return data


def set_members_for_chat(chat_id, snapshot):
    query = f"INSERT INTO DATA (snapshot, chat_id) VALUES('{snapshot}', {chat_id})"
    cursor = conn()
    cursor[0].execute(query)
    cursor[0].close()
    close_conn(cursor[0], cursor[1])


def get_all_chat_id():
    query = f"SELECT DISTINCT chat_id FROM DATA"
    cursor = conn()
    cursor[0].execute(query)
    chat_id_list = cursor[0].fetchall()
    cursor[0].close()
    close_conn(cursor[0], cursor[1])
    return chat_id_list


def get_changelog():
    query = f"SELECT change_log FROM UPDATES WHERE notified IS false"
    cursor = conn()
    cursor[0].execute(query)
    changelog = cursor[0].fetchall()
    cursor[0].close()
    close_conn(cursor[0], cursor[1])
    return changelog


def delete_member_from_db(chat_id, name):
    query = f"DELETE FROM data WHERE chat_id LIKE '{chat_id}' AND snapshot LIKE '{name}%'"
    cursor = conn()
    cursor[0].execute(query)
    cursor[0].close()
    close_conn(cursor[0], cursor[1])


def update_notified():
    query = f"UPDATE UPDATES SET notified=true WHERE notified != true"
    cursor = conn()
    cursor[0].execute(query)
    cursor[0].close()
    close_conn(cursor[0], cursor[1])
