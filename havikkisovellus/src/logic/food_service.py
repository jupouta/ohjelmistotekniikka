from datetime import date

from entities.ingredient import Ingredient


class FoodService:
    
    def __init__(self):
        self.ingredients = []
    
    def add_ingredient(self):
        name = input('Ingredient name: ')
        perishable = input('Is it easily perishable? (yes/no) ')
        perishable_handled = self.add_ingredient_perishable_info(perishable)
        date_today = date.today()
        
        new_ingredient = Ingredient(name, perishable_handled, date_today)
        self.ingredients.append(new_ingredient)
    
    def add_ingredient_perishable_info(self, perishable):
        perishable_handled = None
        if perishable == 'yes':
            perishable_handled = True
        elif perishable == 'no':
            perishable_handled = False
        else:
            perishable_handled = input('Please write \'yes\' or \'no\'.')
        return perishable_handled

    def list_added_ingredients(self):
        for ingredient in self.ingredients:
            print(f'- {ingredient.content}')