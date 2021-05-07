import unittest

from logic.food_service import FoodService



class FakeDatabase:

    def __init__(self):
        self.db = []

    def get_all(self):
        return self.db

    def insert_a_new_ingredient(self, date, ingredient, expire_date, username='testi'):
        index = len(self.db) + 1
        self.db.append((index, date, ingredient, expire_date, 0, username))

    def get_all_ingredients_by_a_user(self, user):
        return_list = []
        for ingr in self.db:
            if ingr[5] == user:
                return_list.append((ingr[0], ingr[1], ingr[2], ingr[3], ingr[4]))
        return return_list

    def mark_ingredient_as_eaten(self, username, ingredient_id):
        for i, ingr in enumerate(self.db):
            if ingr[5] == username and ingr[0] == ingredient_id:
                new_ingr = (ingr[0], ingr[1], ingr[2],
                        ingr[3], 1, ingr[5])
                self.db[i] = new_ingr
                return
        return

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
        self.food_service.database.db = []

    def test_add_ingredient(self):
        self.food_service.add_ingredient(1618207606, 'omena', 1617176770)
        self.assertEqual(len(self.food_service.database.get_all()), 1)

    def test_list_added_ingredients(self):
        self.food_service.add_ingredient(1618207606, 'porkkana', 1618207606, 'testi')
        self.food_service.add_ingredient(1617176770, 'sipuli', 1618207606, 'testi')
        ingredients = self.food_service.list_added_ingredients('testi')
        self.assertEqual(len(ingredients), 2)

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
        self.food_service.add_ingredient(1618207606, 'porkkana', 1618207606, 'testi')
        self.food_service.add_ingredient(1617176770, 'sipuli', 1618207606, 'testi')
        self.food_service.mark_ingredient_as_eaten('testi', 1)

        ingredients = self.food_service.list_added_ingredients('testi', expire=True)
        self.assertEqual(len(ingredients), 1)

        ingredients = self.food_service.list_added_ingredients('testi')
        self.assertEqual(len(ingredients), 2)

        self.food_service.mark_ingredient_as_eaten('testi', 3)

        ingredients = self.food_service.list_added_ingredients('testi', expire=True)
        self.assertEqual(len(ingredients), 1)

        ingredients = self.food_service.list_added_ingredients('testi')
        self.assertEqual(len(ingredients), 2)

    def test_stop_service(self):
        self.food_service.stop_service()
