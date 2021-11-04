import BirthDate
from settings import TOKEN
import telebot
from db_impl import set_members_for_chat

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
                     "/create_new_member - регистрация будущего именинника!\n/help - помощь\n/start - summary бота и Changelog")


@bot.message_handler(commands=['create_new_member'])
def create_new_member(message):
    # ToDo валидация сообщения на формат данных
    new_member_adding = bot.send_message(message.chat.id,
                                         "Ответье на это сообщение форматом:\n*Имя*\n*день* *Месяц на английском* *год*")
    bot.register_for_reply(new_member_adding, step_message)
    # bot.register_next_step_handler(new_member_adding, step_message)


def step_message(message):
    cid = message.chat.id
    userInput = message.text
    list = str(userInput).split("\n")
    set_members_for_chat(message.chat.id, userInput)
    bot.send_message(message.chat.id,
                     f"Вы зарегистрировали пользователя с параметрами:\nИмя: {list[0]}\nДата: {list[1]}")


bot.infinity_polling()
