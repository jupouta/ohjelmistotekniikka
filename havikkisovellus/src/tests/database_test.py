import unittest

from database.initialize_database import initialize_database

from database.database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        initialize_database()
        self.database = Database()

    def test_get_user(self):
        user = self.database.get_user('testi')
        self.assertTrue(user)

        user = self.database.get_user('nimi')
        self.assertFalse(user)

    def test_find_ingredient(self):
        ingredient = self.database.find_ingredient('testi', 'tomaatti')
        self.assertTrue(ingredient)

        ingredient = self.database.find_ingredient('testi', 'sipuli')
        self.assertFalse(ingredient)

