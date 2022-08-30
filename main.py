import telebot

import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):

    # bot.send_message(message.chat.id, f'Привет ✌, {message.from_user.first_name}!')


bot.infinity_polling()
