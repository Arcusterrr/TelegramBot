import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f'Привет ✌, {message.from_user.first_name}!\nПредлагаю тебе зарегистрироваться!\nСкорее нажимай: /register')
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("Зарегистрироваться")
    # markup.add(item1)

@bot.message_handler(commands=['register'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Регистрация")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)

bot.infinity_polling()
