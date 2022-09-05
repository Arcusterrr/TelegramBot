import Data.DataBaseConnection as db

def GetAllHero():
    return db.CURSOR.execute("select * from Hero").fetchone()

def GetYourHero(telegramid_user):
    return db.CURSOR.execute(f"select * from Hero where telegramid_user = {telegramid_user}").fetchone()

db.connection.close()