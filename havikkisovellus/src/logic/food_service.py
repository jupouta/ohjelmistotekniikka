import time

from entities.ingredient import Ingredient
from database import Database

from database_connect import get_database_connection


class FoodService:
    
    def __init__(self):
        self.database = Database()
        self.__connection = get_database_connection()
        self.cursor = self.__connection.cursor()
    
    def add_ingredient(self, name, perishable, date):
        self.database.insert_a_new_ingredient(date, name, perishable, 'testi')

    def list_added_ingredients(self):
        data = self.database.get_all_ingredients_by_a_user('testi')

        ingredients = []
        for row in data:
            ingrdnt, date_added = row[0], row[1]
            ingredient = Ingredient(ingrdnt, date_added)
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
        self.__connection.close()