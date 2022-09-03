import pyodbc
import config

connection = pyodbc.connect(f'Driver={config.DRIVER};'
                            f'Server={config.LOCALHOST};'
                            f'Database={config.DATABASE};'
                            f'Trusted_Connection=yes')

CURSOR = connection.cursor()