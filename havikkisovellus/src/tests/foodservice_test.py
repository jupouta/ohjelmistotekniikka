import unittest

from logic.food_service import FoodService


class FakeDatabase:

    def __init__(self):
        self.db = []

    def get_all(self):
        return self.db

    def insert_a_new_ingredient(self, date, ingredient, expire_date, username='testi'):
        self.db.append((date, ingredient, expire_date, username))

    def get_all_ingredients_by_a_user(self, user):
        return [(1, 'porkkana', 1618207606, 1618207606, 0), (2, 'sipuli', 1618207606, 1618207606, 1)]

    def mark_ingredient_as_eaten(self, username, ingredient_id):
        if ingredient_id == 1:
            return (1, 'tomaatti', 1618207606, 1618207606, 0)

    def get_user(self, username):
        if username == 'testi':
            return ('testi', 'salis')
        return None

    def add_user(self, username, password):
        if username == 'testi':
            return False
        return True

    def stop_service(self):
        pass

class TestFoodService(unittest.TestCase):

    def setUp(self):
        self.database = FakeDatabase()
        self.food_service = FoodService(self.database)

    def test_add_ingredient(self):
        self.food_service.add_ingredient(1618207606, 'omena', 1617176770)
        self.assertEqual(len(self.food_service.database.get_all()), 1)

    def test_list_added_ingredients(self):
        ingredients = self.food_service.list_added_ingredients('testi')
        self.assertEqual(len(ingredients), 2)

        ingredients = self.food_service.list_added_ingredients('testi', expire=True)
        self.assertEqual(len(ingredients), 1)

    def test_check_user(self):
        self.assertTrue(self.food_service.check_username('testi', 'salis'))
        self.assertFalse(self.food_service.check_username('testi', 'salasana'))
        self.assertFalse(self.food_service.check_username('ei', 'salis'))

    def test_add_user(self):
        self.assertFalse(self.food_service.add_user('testi', 'salis'))
        self.assertTrue(self.food_service.add_user('testi1', 'salis'))

    def test_log_out(self):
        self.food_service.log_out()
        self.assertIsNone(self.food_service.user)

    def test_check_date_form(self):
        date = self.food_service.convert_expire_date('22/04/2021')
        self.assertTrue(date > 1600000)

        date = self.food_service.convert_expire_date('')
        self.assertTrue(date > 1600000)

    def test_mark_ingredient_as_eaten(self):
        self.food_service.mark_ingredient_as_eaten('testi', 1)

        ingredients = self.food_service.list_added_ingredients('testi')
        self.assertEqual(ingredients[0].is_used(), 1)
        self.assertEqual(ingredients[0].is_used(), 1)

    #     self.assertTrue(ingredient)
    #     self.assertTrue(ingredient.is_used())

    #     ingredient = self.food_service.mark_ingredient_as_eaten('testi', 'omena')
    #     self.assertFalse(ingredient)

    def test_stop_service(self):
        self.food_service.stop_service()
