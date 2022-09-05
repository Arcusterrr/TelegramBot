from telebot import types

def Buttons():
    markup = types.ReplyKeyboardMarkup()
    buttonInfo = types.KeyboardButton('О персонаже')
    buttonMove = types.KeyboardButton('Move')
    markup.row(buttonInfo, buttonMove)
    return markup
