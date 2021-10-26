import BirthDate
from settings import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Вас приветствует Bro Birthday Bot - бот хранящий инфу о днях рождения ваших бро")


@bot.message_handler(commands=['check_birth'])
def birth_message(message):
    bot.send_message(message.chat.id, f"Дни рождения: \n \n{BirthDate.get_message_birth()}")


bot.infinity_polling()
