import unittest
import time

from datetime import date
from entities.ingredient import Ingredient

class TestIngredient(unittest.TestCase):

    def test_convert_date(self):
        ingredient = Ingredient(1, 'omena', 1618207606, 1619097453)
        self.assertEqual(ingredient.convert_date(1618207606), date(2021, 4, 12))

    def test_is_close_to_perishing_not_true(self):
        days_10_from_today = int(time.time()) + 60*60*24*10
        ingredient = Ingredient(1, 'omena', 1618207606, days_10_from_today)
        self.assertFalse(ingredient.is_close_to_perishing())

    def test_is_close_to_perishing_true(self):
        ingredient = Ingredient(1, 'omena', 1618207606, int(time.time()))
        self.assertTrue(ingredient.is_close_to_perishing())

    def test_get_content(self):
        ingredient = Ingredient(1, 'omena', 1618207606, 1619097453)
        self.assertEqual(ingredient.get_content(), 'omena')

    def test_string(self):
        ingredient = Ingredient(1, 'omena', 1618207606, 1618207606)
        self.assertEqual(ingredient.__str__(), 'omena: added 2021-04-12, expires 2021-04-12, not eaten yet')

        ingredient = Ingredient(1, 'omena', 1618207606, 1618207606, 1)
        self.assertEqual(ingredient.__str__(), 'omena: added 2021-04-12, expires 2021-04-12, already eaten')
