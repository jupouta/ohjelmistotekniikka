from database_connect import get_database_connection

class Database:

    def __init__(self):
        self.__connection = get_database_connection()
        self.cursor = self.__connection.cursor()
        self.cursor.execute('''
            insert into users (username, password) values ('testi', 'salis');
        ''')

        self.cursor.execute('''
            insert into food (date, exp_date, ingredient, username) values (1617176770, 1617176770, 'tomaatti', 'testi');
        ''')

        self.__connection.commit()

    def get_all_ingredients_by_a_user(self, user):
        self.cursor.execute("select ingredient, date, exp_date from food where username=?;",
                            (user, ))
        ingredients = self.cursor.fetchall()
        return ingredients

    def get_user(self, username):
        self.cursor.execute("select username, password from users where username=?;", (username, ))
        user = self.cursor.fetchone()
        return user

    def insert_a_new_ingredient(self, date, ingredient, perishable, username):
        self.cursor.execute(
            "insert into food (date, ingredient, exp_date, username) values (?, ?, ?, ?);",
                            (date, ingredient, perishable, username))
        self.__connection.commit()

    def stop_service(self):
        self.__connection.close()
