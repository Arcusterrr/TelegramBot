import telebot
from Classes import Archer, Knight, Wizard
from UserData.User import User
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f'Привет ✌, {message.from_user.first_name}!\nПредлагаю тебе зарегистрироваться!\nСкорее нажимай: /register')
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("Зарегистрироваться")
    # markup.add(item1)

@bot.message_handler(commands=['register'])
def register_message(message):
    bot.send_message(message.chat.id, 'Выбери класс, которым хочешь быть в гильдии авантюристов: '
                                      '\nРыцарь - /knight'
                                      '\nМаг - /wizard'
                                      '\nЛучник - /archer'
                     )

@bot.message_handler(commands=['knight'])
def reg_knigt(message):
    bot.send_message(message.chat.id, 'Вы зарегистрировались, как Рыцарь')
    user = User(message.from_user.first_name, Knight.Knight)
    bot.send_message(message.chat.id, f'{user.userName}, {user.userClass.name}')

@bot.message_handler(commands=['wizard'])
def reg_wizard(message):
    bot.send_message(message.chat.id, 'Вы зарегистрировались, как Маг')
    user = User(message.from_user.first_name, Wizard.Wizard)
    bot.send_message(message.chat.id, f'{user.userName}, {user.userClass.name}')

@bot.message_handler(commands=['archer'])
def reg_archer(message):
    bot.send_message(message.chat.id, 'Вы зарегистрировались, как Лучник')
    user = User(message.from_user.first_name, Archer.Archer)
    bot.send_message(message.chat.id, f'{user.userName}, {user.userClass.name}')

bot.infinity_polling()
