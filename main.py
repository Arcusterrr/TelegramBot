import telebot
from Classes import Archer, Knight, Wizard
from UserData.User import User
import Data.Extensions.registration as reg
import Data.Extensions.checkUser as checkUser
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    if(checkUser.checkUser(message.from_user.id)):
        bot.send_message(message.chat.id, f'Продолжай совершать подвиги, герой!')
    else:
        bot.send_message(message.chat.id, f'Привет ✌, {message.from_user.first_name}!\nПредлагаю тебе зарегистрироваться!\nСкорее нажимай: /register')

@bot.message_handler(commands=['register'])
def register_message(message):
    if (checkUser.checkUser(message.from_user.id)):
        bot.send_message(message.chat.id, f'Продолжай совершать подвиги, герой!')
    else:
        bot.send_message(message.chat.id, 'Выбери класс, которым хочешь быть в гильдии авантюристов: '
                                          '\nРыцарь - /knight'
                                          '\nМаг - /wizard'
                                          '\nЛучник - /archer'
                                          '\n❗️❗️❗️Класс сменить будет нельзя, помни об этом❗️❗️❗️'
                         )

@bot.message_handler(commands=['knight'])
def reg_knigt(message):
    user = User(message.from_user.first_name, Knight.Knight, message.from_user.id)
    bot.send_message(message.chat.id, reg.registration(user.userName, user.userClass.name, user.userTelegramId))

@bot.message_handler(commands=['wizard'])
def reg_wizard(message):
    user = User(message.from_user.first_name, Wizard.Wizard, message.from_user.id)
    bot.send_message(message.chat.id, reg.registration(user.userName, user.userClass.name, user.userTelegramId))


@bot.message_handler(commands=['archer'])
def reg_archer(message):
    user = User(message.from_user.first_name, Archer.Archer, message.from_user.id)
    bot.send_message(message.chat.id, reg.registration(user.userName, user.userClass.name, user.userTelegramId))


bot.infinity_polling()
