import os
import sqlite3

directory_name = os.path.dirname(__file__)
connection = sqlite3.connect(os.path.join(directory_name, "data", "database.sqlite"))
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection