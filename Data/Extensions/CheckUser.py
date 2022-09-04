import Data.DataBaseConnection as db

def checkUser(telegramid_user):
    user = db.CURSOR.execute(f"select * from UsersDB where (telegramid_user = '{telegramid_user}')")
    if user.fetchone() is not None:
        return True
    else:
        return False
