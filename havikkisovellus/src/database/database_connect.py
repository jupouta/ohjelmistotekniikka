import sqlite3

from config import DATA_FILENAME

connection = sqlite3.connect(DATA_FILENAME)
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection
