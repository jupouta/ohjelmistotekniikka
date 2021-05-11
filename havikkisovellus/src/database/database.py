"""Class and methods for handling all the database transactions."""
from database.database_connect import get_database_connection

class Database:
    """Class for handling all the database transactions.

    Attributes:
        connection: The database connection.
        cursor: The cursor which performs the database transactions."""

    def __init__(self):
        """Class instructor.
        Automatically adds one test user and two test ingredients."""
        self._connection = get_database_connection()
        self._cursor = self._connection.cursor()

        self._initialize()

    def _initialize(self):
        """Initialize the database.
        Add a test user to the database, if not already there."""
        if not self.get_user('testi'):
            self._cursor.execute('''
               insert into users (username, password) values ('testi', 'salis');
            ''')
        self._connection.commit()

    def get_all_ingredients_by_a_user(self, username):
        """Return all the ingredients a user has added.
        Args:
            username: The user's username.
        Returns: A list of the user's ingredients."""
        self._cursor.execute(
            "select id, date, ingredient, exp_date, used from food where username=?;",
                            (username, ))
        ingredients = self._cursor.fetchall()
        return ingredients

    def get_user(self, username):
        """Return the user with the given username.
        Args:
            username: The user's username.
        Returns: The found username and password."""
        self._cursor.execute("select username, password from users where username=?;",
                              (username, ))
        user = self._cursor.fetchone()
        return user

    def add_user(self, username, password):
        """Add a user with given username and password to the database.

        Args:
            username: The username for the user.
            password: The password for the user."""
        self._cursor.execute('''
            insert into users (username, password) values (?, ?);''',
            (username, password))
        self._connection.commit()

    def find_ingredient(self, username, ingredient_id):
        """Find the user's ingredient with given ingredient id (in the database).
        Return the found ingredient.

        Args:
            username: The user's username.
            ingredient_id: The id for the ingredient in the database.
        Returns:
            The found ingredient."""
        self._cursor.execute(
            '''select id, date, ingredient, exp_date, used, username from food
            where username=? and id=?;''', (username, ingredient_id))
        ingredient = self._cursor.fetchone()
        return ingredient

    def mark_ingredient_as_eaten(self, username, ingredient_id):
        """Mark the given ingredient as eaten.

        Args:
            username: The user's username.
            ingredient_id: The id of the ingredient to be marked."""
        self._cursor.execute(
            '''update food
            set used=1
            where username=? and id=?;''', (username, ingredient_id))
        self._connection.commit()

    def insert_a_new_ingredient(self, date, ingredient, expire_date, username):
        self._cursor.execute(
            "insert into food (date, ingredient, exp_date, username) values (?, ?, ?, ?);",
                            (date, ingredient, expire_date, username))
        self._connection.commit()

    def delete_users(self):
        self._cursor.execute('delete from users;')
        self._connection.commit()

    def delete_ingredients(self):
        self._cursor.execute('delete from food;')
        self._connection.commit()

    def delete_all(self):
        self.delete_ingredients()
        self.delete_users()

    def stop_service(self):
        self._connection.close()
