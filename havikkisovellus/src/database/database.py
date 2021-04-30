from database.database_connect import get_database_connection

class Database:
    """Class for handling all the database transactions.

    Attributes:
        connection: The database connection.
        cursor: The cursor which performs the database transactions."""

    def __init__(self):
        """Class instructor.
        Automatically adds one test user and two test ingredients."""
        self.__connection = get_database_connection()
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute('''
            insert into users (username, password) values ('testi', 'salis');
        ''')

        self.__cursor.execute('''
            insert into food (date, exp_date, ingredient, username) values (1617176770, 1617176770, 'tomaatti', 'testi');
        ''')
        self.__cursor.execute('''
            insert into food (date, exp_date, ingredient, username) values (1618207606, 1619506554, 'omena', 'testi');
        ''')

        self.__connection.commit()

    def get_all_ingredients_by_a_user(self, user):
        self.__cursor.execute("select ingredient, date, exp_date, used from food where username=?;",
                            (user, ))
        ingredients = self.__cursor.fetchall()
        return ingredients

    def get_user(self, username):
        self.__cursor.execute("select username, password from users where username=?;",
                              (username, ))
        user = self.__cursor.fetchone()
        return user

    def add_user(self, username, password):
        self.__cursor.execute('''
            insert into users (username, password) values (?, ?);''',
            (username, password))
        self.__connection.commit()

    def find_ingredient(self, username, ingredient_name):
        self.__cursor.execute(
            '''select ingredient, date, exp_date, used from food
            where username=? and ingredient=?;''', (username, ingredient_name))
        ingredient = self.__cursor.fetchone()
        return ingredient

    def mark_ingredient_as_eaten(self, username, ingredient_name):
        self.__cursor.execute(
            '''update food
            set used=1
            where username=? and ingredient=?;''', (username, ingredient_name))
        ingredient = self.find_ingredient(username, ingredient_name)
        return ingredient

    def insert_a_new_ingredient(self, date, ingredient, expire_date, username):
        self.__cursor.execute(
            "insert into food (date, ingredient, exp_date, username) values (?, ?, ?, ?);",
                            (date, ingredient, expire_date, username))
        self.__connection.commit()

    def delete_users(self):
        self.__cursor.execute('delete from users;')
        self.__connection.commit()

    def delete_ingredients(self):
        self.__cursor.execute('delete from food;')
        self.__connection.commit()

    def delete_all(self):
        self.delete_ingredients()
        self.delete_users()

    def stop_service(self):
        self.__connection.close()
