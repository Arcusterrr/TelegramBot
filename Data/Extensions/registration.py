import Data.DataBaseConnection as db

def registration(name_user, class_user, telegramid_user):
    db.CURSOR.execute(f'insert into TelegramUsers (name_user, class_user, telegramid_user) '
                      f'values ({name_user}, {class_user}, {telegramid_user})')
