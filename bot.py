import BirthDate
from settings import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Вас приветствует Bro Birthday Bot - бот хранящий инфу о днях рождения ваших бро")


@bot.message_handler(commands=['check_birth'])
def birth_message(message):
    bot.send_message(message.chat.id, f"Дни рождения в этом месяце: \n \n{BirthDate.get_message_birth()}")


@bot.message_handler(commands=['all'])
def all_birth(message):
    bot.send_message(message.chat.id, BirthDate.get_all_birth())


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     "Доступные команды: \n \n/all - все дни рождения\n/check_birth - Дни рождения +- 14 дней\n/help - помощь\n")


bot.infinity_polling()
