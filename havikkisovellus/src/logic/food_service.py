"""Class and methods for doing the logic between the UI
and database transactions."""
import time
import datetime

from entities.ingredient import Ingredient
from entities.user import User


class FoodService:
    """Class for doing the logic between the UI
    and database transactions.

    Attributes:
        database: The database for retrieving and adding data.
        user: The user of this session.
    """

    def __init__(self, database):
        """The constructor for the class.

        Args:
            database: The database for retrieving and adding data.
        """
        self.database = database
        self.user = None

    def check_username(self, given_username, given_password):
        """Checks that a) the username is found in the database
        b) the password corresponds to the username.

        Args:
            given_username: The username given by the user.
            given_password: The password given by the user.

        Returns:
            If the user is found and it corresponds
            the password, returns True; otherwise False."""
        user_retrieved = self.database.get_user(given_username)
        if user_retrieved:
            username, password = user_retrieved[0], user_retrieved[1]
            self.user = User(username, password)
            if given_password == password:
                return True
        return False

    def get_user(self):
        """Return the user loggied in in this session.
        Returns:
            The user in this session."""
        return self.user

    def add_user(self, username, password):
        """Add user to the database if the username doesn't exist already.
        Args:
            username: The username given by user.
            password: The password given by user.

        Returns:
            Boolean value indicating if the new username is accepted.
            If it already exists, False is returned."""
        user = self.database.get_user(username)
        if user:
            return False
        self.database.add_user(username, password)
        return True

    def log_out(self):
        self.user = None

    def convert_expire_date(self, date):
        """Convert the given expire date to timestamp format (integer).
        Check that the date conforms to the format 'dd/mm/yyyy'.
        If date is empty, add the expire date to 10 days from today.

        Args:
            date: The date given in the format 'dd/mm/yyyy'.

        Returns:
            The given expiration date as timestamp integer."""

        if date == '':
            perishable_date = time.time() + 60*60*24*10
        else:
            perishable_date = time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())
        return int(perishable_date)

    def add_ingredient(self, date, ingredient, expire_date, username='testi'):
        """Add a new ingredient to the database.

        Args:
            date:
                The date when the ingredient has been added in timestamp format (integer).
            ingredient: The name of the ingredient.
            expire_date: The date when the ingredient will expire.
            username: The user's username. If not given, 'testi' will be used.
        """
        self.database.insert_a_new_ingredient(date, ingredient, expire_date, username)

    # TODO: self.user
    def mark_ingredient_as_eaten(self, username, ingredient_id):
        """Mark an ingredient as used.
        Return the marked ingredient for further use.

        Args:
            username: The user's username.
            ingredient_id: The id of the ingredient to be marked."""
        self.database.mark_ingredient_as_eaten(username, ingredient_id)

    def list_added_ingredients(self, username, expire=False):
        """List user's ingredients found in the database.
        Iterate through and add all the ingredients or
        the ones that are close to expiring.

        Args:
            username:
                The user's username.
            expire:
                Optional;
                List ingredients close to expiring (True) or
                all the ingredients (False).
                All ingredients returned if argument not given.

        Returns:
            A list of the ingredients according to given conditions."""
        data = self.database.get_all_ingredients_by_a_user(username)

        ingredients = []
        for row in data:
            ingr_id, ingr, date_added, date_expires, used = row[0], row[1], row[2], row[3], row[4]
            ingredient = Ingredient(ingr_id, ingr, date_added, date_expires, used)
            if expire:
                if ingredient.is_close_to_perishing() and not ingredient.is_used():
                    ingredients.append(ingredient)
            else:
                ingredients.append(ingredient)

        return ingredients

    def stop_service(self):
        """Stop the database, and hence the app."""
        self.database.stop_service()
