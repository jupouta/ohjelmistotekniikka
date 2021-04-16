import unittest

from logic.food_service import FoodService


class FakeDatabase:

    def __init__(self):
        self.db = []

    def get_all(self):
        return self.db

    def insert_a_new_ingredient(self, date, ingredient, perishable, username='testi'):
        self.db.append((date, ingredient, perishable, username))

    def get_all_ingredients_by_a_user(self, user):
        return [('porkkana', 1618207606, 1618207606), ('sipuli', 1618207606, 1618207606)]

    def get_user(self, username):
        return ('testi', 'salasana')

    def stop_service(self):
        pass

class TestFoodService(unittest.TestCase):

    def setUp(self):
        self.food_service = FoodService(FakeDatabase())

    def test_add_ingredient(self):
        self.food_service.add_ingredient('omena', 1618207606, 1617176770)
        self.assertEqual(len(self.food_service.database.get_all()), 1)

    def test_list_added_ingredients(self):
        ingredients = self.food_service.list_added_ingredients('testi')
        self.assertEqual(len(ingredients), 2)