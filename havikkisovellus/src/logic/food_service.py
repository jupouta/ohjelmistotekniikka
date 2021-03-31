import time
import datetime 

from entities.ingredient import Ingredient
from database_connect import get_database_connection


class FoodService:
    
    def __init__(self):
        self.__connection = get_database_connection()
        self.cursor = self.__connection.cursor()

        self.cursor.execute('''
            insert into users (username,password) values ('paltu', 'paltu123');
        ''')
        
        self.cursor.execute('''
            insert into food (date, exp_date, ingredient, username) values (1617176770,1617176770, 'tomaatti', 'paltu');
        ''')

        self.__connection.commit()
    
    def add_ingredient(self):
        name = input('Ingredient name: ')
        perishable = input('Is it easily perishable? (yes/no) ')
        perishable_handled = self.add_ingredient_perishable_info(perishable)
        time_time = int(time.time())
        
        new_ingredient = Ingredient(name, perishable_handled, time_time)   # TODO
        self.cursor.execute("insert into food (date, ingredient, perishable) values (?, ?, ?);",
                            (time_time, name, perishable_handled))
        self.__connection.commit()
    
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
        self.cursor.execute("select ingredient, date from food;")
        
        
        for row in self.cursor:
            print(f'{row[0]}: {row[1]}')
            print(datetime.datetime.fromtimestamp(row[1]))

    
    def show_soon_perishable_ingredients(self):
        self.cursor.execute("select * from food;")
        
        for row in self.cursor:
            row_date = int(row[3])
            print(row_date < time.time())
            print(time.localtime(row_date))
            # TODO: luokka, jossa vaihdetaan
    
    def stop_service(self):
        self.__connection.close()