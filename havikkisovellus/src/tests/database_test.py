import unittest

from database.initialize_database import initialize_database

from database.database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        initialize_database()
        self.database = Database()

    def test_assert_test(self):
        self.assertTrue(True)
