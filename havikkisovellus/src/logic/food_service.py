import time
import datetime

from entities.ingredient import Ingredient


class FoodService:

    def __init__(self, database):
        self.database = database

    def check_username(self, given_username, given_password):
        user = self.database.get_user(given_username)
        if user:
            password = user[1]
            if given_password == password:
                return True
        return False

    def check_date_form(self, date):
        if date == '':
            perishable_date = time.time() + 60*60*24*10
        else:
            perishable_date = time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())
        return int(perishable_date)

    def add_ingredient(self, date, date_expires, name):
        self.database.insert_a_new_ingredient(date, name, date_expires, 'testi')

    def mark_ingredient_as_eaten(self, username, ingredient_name):
        retrieved = self.database.mark_ingredient_as_eaten(username, ingredient_name)
        if retrieved:
            ingrdnt, date_added, date_expires, used = retrieved[0], retrieved[1], retrieved[2], retrieved[3]
            ingredient = Ingredient(ingrdnt, date_added, date_expires, used)
            return ingredient
        else:
            print('No ingredient found!')

    def list_added_ingredients(self, username, expire=False):
        data = self.database.get_all_ingredients_by_a_user(username)

        ingredients = []
        for row in data:
            ingrdnt, date_added, date_expires = row[0], row[1], row[2]
            ingredient = Ingredient(ingrdnt, date_added, date_expires)
            if expire:
                # TODO: älä lisää merkittyjä
                if ingredient.is_close_to_perishing():
                    ingredients.append(ingredient)
            else:
                ingredients.append(ingredient)

        return ingredients

    def stop_service(self):
        self.database.stop_service()
