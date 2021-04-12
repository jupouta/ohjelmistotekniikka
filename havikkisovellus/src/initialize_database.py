
from database_connect import get_database_connection


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
        create table food (
            id integer primary key autoincrement,
            date int,
            exp_date int,
            ingredient text,
            username text not null,
            foreign key (username)
                references users (username)
        );
    ''')

    cursor.execute('''
        create table users (
            id integer primary key autoincrement,
            username text not null unique,
            password text not null
        );
    ''')

    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

    #connection.close()

#if __name__ == '__main__':
#    initialize()
