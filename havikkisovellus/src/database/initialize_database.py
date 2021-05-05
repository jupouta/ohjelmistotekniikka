from database.database_connect import get_database_connection
from config import ENVIRONMENT

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists food;
    ''')
    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table if not exists food (
            id integer primary key autoincrement,
            date int,
            exp_date int,
            ingredient text,
            used int,
            username text not null,
            foreign key (username)
                references users (username)
        );
    ''')

    cursor.execute('''
        create table if not exists users (
            id integer primary key autoincrement,
            username text not null unique,
            password text not null
        );
    ''')

    connection.commit()

def initialize_database():
    connection = get_database_connection()
    if ENVIRONMENT == 'test':
        drop_tables(connection)
    create_tables(connection)

    #connection.close()

#if __name__ == '__main__':
#    initialize()
