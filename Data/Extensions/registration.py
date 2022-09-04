import Data.DataBaseConnection as db
import Data.Extensions.checkUser as checkUser

def registration(name_user, class_user, telegramid_user):
    if not checkUser.checkUser(telegramid_user):
        db.CURSOR.execute(f"insert into UsersDB (name_user, class_user, telegramid_user) values ('{name_user}', '{class_user}', {telegramid_user})")
        db.CURSOR.commit()
        print(f'Пользователь: {name_user} зарегистрировался')
        return "Вы зарегистрировались"
    else:
        return "Вы уже зарегистрированы"
