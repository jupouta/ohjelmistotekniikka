import os
import sqlite3

dirname = os.path.dirname(__file__)
file_name = os.path.join(dirname, "..", "data", "database.sqlite")
connection = sqlite3.connect(file_name)
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection