import BirthDate
from settings import TOKEN
import telebot
from db_impl import set_members_for_chat

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Вас приветствует Bro Birthday Bot - бот хранящий инфу о днях рождения ваших бро"
                     "\n\nChangelog:"
                     "\n(v0.2)"
                     "\n- добавлена сортировка по возрастанию относительно текущей даты для команды /all"
                     "\n- добавлено акцентирование внимания на ближайшем др в команде /all"
                     "\n- произведена русификация имен"
                     "\n\n(v0.3)"
                     "\n- мониторинг др командой /check_birth увеличен до 31 одного дня (в рамках одного месяца)"
                     "\n- добавлена сортировка по возрастанию для команды /check_birth"
                     "\n- реализован мэппинг номера месяца на слово месяца")


@bot.message_handler(commands=['check_birth'])
def birth_message(message):
    bot.send_message(message.chat.id, f"Дни рождения в этом месяце: \n \n{BirthDate.get_message_birth(message.chat.id)}")


@bot.message_handler(commands=['all'])
def all_birth(message):
    bot.send_message(message.chat.id, BirthDate.get_all_birth(message.chat.id))


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     "Доступные команды: \n \n/all - все дни рождения\n/check_birth - Дни рождения текущего месяца\n/help - помощь\n/start - summary бота и Changelog")


@bot.message_handler(commands=['create_new_member'])
def create_new_member(message):
    # ToDo валидация сообщения на формат данных
    new_member_adding = bot.send_message(message.chat.id, "Введите сообщение формата:\n*Имя*\n*день* *Месяц на английском* *год*")
    bot.register_next_step_handler(new_member_adding, step_message)


def step_message(message):
    cid = message.chat.id
    userInput = message.text
    list = str(userInput).split("\n")
    set_members_for_chat(message.chat.id, userInput)
    bot.send_message(message.chat.id,
                     f"Вы зарегистрировали пользователя с параметрами:\nИмя: {list[0]}\nДата: {list[1]}")


bot.infinity_polling()
