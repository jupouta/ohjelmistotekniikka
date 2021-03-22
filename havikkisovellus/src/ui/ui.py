from entities.ingredient import Ingredient

from datetime import date


class UI:
    
    def __init__(self):
        self.ingredients = []
    
    def start(self):
        print('Starting food waste app..')
        print('\n')
        print('Add new ingredient:')
        name = input('Ingredient name:')
        perishable = input('Is it easily perishable? (yes/no)')
        date_today = date.today()
        self.add_ingredient(name, perishable, date_today)
        
        
    def add_ingredient(self, name, perishable, date_today):
        new_ingredient = Ingredient(name, perishable, date_today)