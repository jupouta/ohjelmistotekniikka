from logic.food_service import FoodService

class UI:
    
    def __init__(self):
        self.food_service = FoodService()
    
    def start(self):
        print('Starting food waste app..')
        print('\n')
        self.print_commands()
        
        while True:
            print('\n')
            given_command = input('Write your command: ')
            
            if given_command == 'list':
                self.food_service.list_added_ingredients()
            elif given_command == 'add':
                self.food_service.add_ingredient()
            elif given_command == 'print':
                self.print_commands()
            elif given_command == 'stop':
                self.food_service.stop_service()
                print('Bye!')
                break
            else:
                print('Something happened.. Please write again.')
    
    def print_commands(self):
        print('Commands:')
        print('List all the ingredients - write \'list\'')
        print('Add new ingredient - write \'add\'')
        print('Stop the program - write \'stop\'')
        print('Show the commands - write \'print\'')