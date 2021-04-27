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
        return [('porkkana', 1618207606, 1618207606, 0), ('sipuli', 1618207606, 1618207606, 1)]

    def mark_ingredient_as_eaten(self, username, ingredient_name):
        if ingredient_name == 'tomaatti':
            return ('tomaatti', 1618207606, 1618207606, 1)
        return None

    def get_user(self, username):
        if username == 'testi':
            return ('testi', 'salis')
        return None

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

        ingredients = self.food_service.list_added_ingredients('testi', expire=True)
        self.assertEqual(len(ingredients), 1)

    def test_check_user_works(self):
        self.assertTrue(self.food_service.check_username('testi', 'salis'))

    def test_check_user_password(self):
        self.assertFalse(self.food_service.check_username('testi', 'salasana'))

    def test_check_user_does_not_work(self):
        self.assertFalse(self.food_service.check_username('ei', 'salis'))

    def test_check_date_form(self):
        date = self.food_service.check_date_form('22/04/2021')
        self.assertTrue(date > 1600000)

        date = self.food_service.check_date_form('')
        self.assertTrue(date > 1600000)

    def test_mark_ingredient_as_eaten(self):
        ingredient = self.food_service.mark_ingredient_as_eaten('testi', 'tomaatti')
        self.assertTrue(ingredient)
        self.assertTrue(ingredient.is_used())

        ingredient = self.food_service.mark_ingredient_as_eaten('testi', 'omena')
        self.assertFalse(ingredient)

    def test_stop_service(self):
        self.food_service.stop_service()
