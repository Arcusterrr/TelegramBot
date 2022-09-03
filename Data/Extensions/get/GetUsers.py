import Data.DataBaseConnection as db

db.CURSOR.execute("select * from TelegramUsers")

db.connection.close()
