import unittest

from database.initialize_database import initialize_database

from database.database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        initialize_database()
        self.database = Database()
        self.database.delete_all()

    def test_add_user(self):
        self.database.add_user('testi', 'salis')
        self.database.add_user('testi123', 'salis')

        user = self.database.get_user('testi')
        self.assertTrue(user)

        user = self.database.get_user('testi123')
        self.assertTrue(user)

        user = self.database.get_user('esimerkki')
        self.assertFalse(user)

    def test_find_all_users_ingredients(self):
        self.database.insert_a_new_ingredient(1619778769, 'tomaatti', 1619778769, 'testi')
        self.database.insert_a_new_ingredient(1619778769, 'omena', 1619778769, 'testi')
        self.database.insert_a_new_ingredient(1619778769, 'omena', 1619778769, 'testi123')

        ingredients = self.database.get_all_ingredients_by_a_user('testi')
        self.assertEqual(len(ingredients), 2)

        ingredients = self.database.get_all_ingredients_by_a_user('testi123')
        self.assertEqual(len(ingredients), 1)

    def test_mark_ingredient_as_eaten(self):
        self.database.insert_a_new_ingredient(1619778769, 'tomaatti', 1619778769, 'testi')
        self.database.mark_ingredient_as_eaten('testi', 1)

        ingredients = self.database.get_all_ingredients_by_a_user('testi')
        ingredient = ingredients[0]

        self.assertEqual(ingredient[4], 1)

        #ingredient = self.database.mark_ingredient_as_eaten('testi', 'sipuli')
        #self.assertFalse(ingredient)

    def tearDown(self):
        self.database.delete_all()
