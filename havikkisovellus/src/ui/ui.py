import time

class UI:

    def __init__(self, food_service):
        self.food_service = food_service

    def start(self):
        print('Starting food waste app..')
        print('\n')
        self.start_login()

    def start_login(self):
        print('Login:')

        while True:
            given_username = input('Username: ')
            given_password = input('Password: ')

            if self.food_service.check_username(given_username, given_password):
                break
            print('Username or password not found!')

        self.start_program()

    def start_program(self):
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
                break
            else:
                print('Something happened.. Please write again.')

    def list_added_ingredients(self):
        ingredients = self.food_service.list_added_ingredients()
        for ingredient in ingredients:
            print(ingredient)

    def add_new_ingredient(self):
        name = input('Ingredient name: ')
        date_expires = self.add_ingredient_perishable_info()
        date = int(time.time())
        self.food_service.add_ingredient(date, date_expires, name)

    def add_ingredient_perishable_info(self):
        print('Add expiration date: ')
        print('(If none given, 10 days will be the default.)')
        print('NB! Use the form \'dd/mm/yyyy\'')

        while True:
            given_date = input('Expiration date: ')
            try:
                timestamp = self.food_service.check_date_form(given_date)
                break
            except ValueError:
                print('Oops! Remember to give the date in the correct form dd/mm/yyyy.')
        return timestamp

    def print_commands(self):
        print('Commands:')
        print('List all the ingredients - write \'list\'')
        print('Add new ingredient - write \'add\'')
        print('Stop the program - write \'stop\'')
        print('Show the commands - write \'print\'')

    def stop_service(self):
        self.food_service.stop_service()
        print('Bye!')
