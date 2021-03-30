
from database_connect import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists foodtable;
    ''')
    cursor.execute('''
        drop table if exists food;
    ''')
    cursor.execute('''
        drop table if exists mytable;
    ''')

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table food (
            id integer primary key autoincrement,
            ingredient text,
            perishable boolean,
            date text
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