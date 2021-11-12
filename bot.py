import datetime

import BirthDate
from settings import TOKEN
import telebot
import schedule
from db_impl import set_members_for_chat, get_all_chat_id, get_changelog, \
    delete_member_from_db, update_notified
from alert_sheduler import schedule_checker
from threading import Thread

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Вас приветствует Bro Birthday Bot - бот хранящий инфу о днях рождения ваших бро"
                     "\n\nНаписан на Python, дни рождения хранятся в PostgreSQL для каждого чата отдельно основываясь на связи с сhat_id (подробнее в API Telegram)"
                     "\n\nКстати, буду рад звездочкам за костылики в open source - https://github.com/OrangeCoderRU/bro-birthsday-bot"
                     "\n\nПопробуй /help, чтобы узнать доступные функции!")


@bot.message_handler(commands=['check_birth'])
def birth_message(message):
    bot.send_message(message.chat.id,
                     f"Дни рождения в этом месяце: \n \n{BirthDate.get_message_birth(message.chat.id)}")


@bot.message_handler(commands=['all'])
def all_birth(message):
    bot.send_message(message.chat.id, BirthDate.get_all_birth(message.chat.id))


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     "Доступные команды: \n \n/all - все дни рождения\n/check_birth - Дни рождения текущего месяца\n"
                     "/create_new_member - регистрация будущего именинника!\n/help - помощь\n/start - summary бота и Changelog"
                     "\n/delete_member - удаление пользователя")


@bot.message_handler(commands=['create_new_member'])
def create_new_member(message):
    # ToDo валидация сообщения на формат данных
    new_member_adding = bot.send_message(message.chat.id,
                                         "Ответье на это сообщение форматом:\n*Имя*\n*день* *Месяц на английском* *год*")
    bot.register_for_reply(new_member_adding, step_message_for_adding)
    # bot.register_next_step_handler(new_member_adding, step_message)


@bot.message_handler(commands=['delete_member'])
def delete_member(message):
    member_deleting = bot.send_message(
        message.chat.id, "Ответьте на это сообщение именем человека, которого вы хотите удалить, "
                         "ровно также как оно указано в команде /all")

    bot.register_for_reply(member_deleting, step_message_for_deleting)


def step_message_for_adding(message):
    cid = message.chat.id
    userInput = message.text
    list = str(userInput).split("\n")
    set_members_for_chat(message.chat.id, userInput)
    bot.send_message(message.chat.id,
                     f"Вы зарегистрировали пользователя с параметрами:\nИмя: {list[0]}\nДата: {list[1]}")


def step_message_for_deleting(message):
    userInput = message.text
    list = str(userInput).split("\n")
    delete_member_from_db(message.chat.id, userInput)
    bot.send_message(message.chat.id,
                     f"Вы удалили пользователя с именем {list[0]}, если он существовал, проверить снова - /all")


def alerting_about_birthday():
    actual_birth = BirthDate.get_today_birth()
    today = datetime.datetime.now()
    if len(actual_birth) != 0:
        for birth in actual_birth:
            return bot.send_message(chat_id=birth[1],
                                    text=f"Сегодня день рождения у {birth[0][0]}, поздравляем!\nЕму/ей {today.year - birth[0][1].tm_year}")
    else:
        return None


if __name__ == "__main__":
    list_chat_id = get_all_chat_id()
    changelog = get_changelog()
    if len(changelog) != 0:
        for chat_id in list_chat_id:
            bot.send_message(chat_id=chat_id[0], text=f'Вышло обновление:\n\n{changelog[0][0]}')

    update_notified()

    schedule.every().day.at("07:00").do(alerting_about_birthday)
    Thread(target=schedule_checker).start()

bot.infinity_polling()
