import Data.DataBaseConnection as db

db.CURSOR.execute("select * from Hero")

db.connection.close()