import time

from logic.food_service import FoodService

class UI:
    
    def __init__(self, food_service):
        self.food_service = food_service
    
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
                self.add_new_ingredient()
            elif given_command == 'print':
                self.print_commands()
            elif given_command == 'stop':
                self.stop_service()
                print('Bye!')
                break
            else:
                print('Something happened.. Please write again.')
    
    def list_added_ingredients(self):
        ingredients = self.food_service.list_added_ingredients()
        for ingredient in ingredients:
            print(ingredient)
        
    def add_new_ingredient(self):
        name = input('Ingredient name: ')
        perishable = self.add_ingredient_perishable_info()
        date = int(time.time())
        self.food_service.add_ingredient(name, perishable, date)
    
    def add_ingredient_perishable_info(self):
        perishable = input('Is it easily perishable? (yes/no) ')

        # TODO
        if perishable in ['yes', 'y']:
            date = int(time.time())
        elif perishable in ['no', 'n']:
            date = int(time.time())
        else:
            perishable_handled = input('Please write \'yes\' or \'no\'.')
            date = int(time.time())
        return date
    
    def print_commands(self):
        print('Commands:')
        print('List all the ingredients - write \'list\'')
        print('Add new ingredient - write \'add\'')
        print('Stop the program - write \'stop\'')
        print('Show the commands - write \'print\'')
    
    def stop_service(self):
        self.food_service.stop_service()