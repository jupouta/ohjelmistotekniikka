from sqlite3.dbapi2 import connect
from database_connect import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists foodtable;
    ''')
    cursor.execute('''
        drop table if exists mytable;
    ''')

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table foodtable (
            id text primary key,
            column text
        );
    ''')

    connection.commit()

def initialize():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    
    connection.close()

if __name__ == "__main__":
    initialize()