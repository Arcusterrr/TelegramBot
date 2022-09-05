import Data.DataBaseConnection as db
import Data.Extensions.checkUser as checkUser
from UserData.User import User

def registration(user):
    if not checkUser.checkUser(user.userTelegramId):
        db.CURSOR.execute(f"insert into Hero (telegramid_user, hp_hero, damage_hero, armor_hero, mana_hero) "
                          f"values ('{user.userTelegramId}', "
                          f"{user.userClass.hp}, "
                          f"{user.userClass.damage}, "
                          f"{user.userClass.armor}, "
                          f"{user.userClass.mana})"
                          )
        db.CURSOR.commit()
        db.CURSOR.execute(f"insert into UsersDB (name_user, class_user, telegramid_user) values ('{user.userName}', '{user.userClass.name}', {user.userTelegramId})")
        db.CURSOR.commit()
        print(f'Пользователь: {user.userName} зарегистрировался')
        return "Вы зарегистрировались"
    else:
        return "Вы уже зарегистрированы"
