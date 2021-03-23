from logic.food_service import FoodService
from entities.ingredient import Ingredient

from datetime import date


class UI:
    
    def __init__(self):
        self.ingredients = []
    
    def start(self):
        print('Starting food waste app..')
        print('\n')
        self.print_commands()
        
        while True:
            print('\n')
            given_command = input('Write your command: ')
            
            if given_command == 'list':
                self.list_added_ingredients()
            elif given_command == 'add':
                self.add_ingredient()
            elif given_command == 'print':
                self.print_commands()
            elif given_command == 'stop':
                print('Bye!')
                break
            else:
                print('Something happened.. Please write again.')
    
    def list_added_ingredients(self):
        for ingredient in self.ingredients:
            print(f'- {ingredient.content}')
        
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
    
    def print_commands(self):
        print('Commands:')
        print('List all the ingredients - write \'list\'')
        print('Add new ingredient - write \'add\'')
        print('Stop the program - write \'stop\'')
        print('Show the commands - write \'print\'')