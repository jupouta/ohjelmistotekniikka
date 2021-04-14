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

    def list_added_ingredients(self):
        data = self.database.get_all_ingredients_by_a_user('testi')

        ingredients = []
        for row in data:
            ingrdnt, date_added, date_expires = row[0], row[1], row[2]
            ingredient = Ingredient(ingrdnt, date_added, date_expires)
            ingredients.append(ingredient)

        return ingredients

    # TODO: combine with upper one?
    def show_soon_perishable_ingredients(self):
        data = self.database.get_all_ingredients_by_a_user('testi')

        ingredients = []
        for row in data:
            ingrdnt, date_added = row[0], row[1]
            ingredient = Ingredient(ingrdnt, date_added)

            if ingredient.is_close_to_perishing():
                ingredients.append(ingredient)
        return ingredients

    def stop_service(self):
        self.database.stop_service()
