import unittest

from logic.food_service import FoodService

class TestFoodService(unittest.TestCase):
    
    def setUp(self):
        self.food_service = FoodService()
    