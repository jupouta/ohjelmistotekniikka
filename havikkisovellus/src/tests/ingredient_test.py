import unittest

from datetime import date
from entities.ingredient import Ingredient

class TestIngredient(unittest.TestCase):

    def test_convert_date(self):
        ingredient = Ingredient('omena', 1618207606, 1619097453)
        self.assertEqual(ingredient.convert_date(1618207606), date(2021, 4, 12))

    def test_is_close_to_perishing(self):
        ingredient = Ingredient('omena', 1618207606, 1619097453)
        self.assertFalse(ingredient.is_close_to_perishing())
