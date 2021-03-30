from datetime import date

from entities.ingredient import Ingredient
from database_connect import get_database_connection


class FoodService:
    
    def __init__(self):
        self.date_today = date.today()
        
        self.__connection = get_database_connection()
        self.cursor = self.__connection.cursor()

        self.cursor.execute('''
            insert into food (ingredient, perishable, date) values ('tomaatti', true, '2021-3-25');
        ''')

        self.__connection.commit()
    
    def add_ingredient(self):
        name = input('Ingredient name: ')
        perishable = input('Is it easily perishable? (yes/no) ')
        perishable_handled = self.add_ingredient_perishable_info(perishable)
        
        new_ingredient = Ingredient(name, perishable_handled, self.date_today)   # TODO
        self.cursor.execute("insert into food (ingredient, perishable, date) values (?, ?, ?);",
                            (name, perishable_handled, self.date_today))
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
        self.cursor.execute("select * from food;")
        for row in self.cursor:
            print(f'{row[0]}: {row[1]} {row[3]}')
        
        self.show_soon_perishable_ingredients()
    
    def show_soon_perishable_ingredients(self):
        self.cursor.execute("select * from food;")
        
        for row in self.cursor:
            row_date = row[3]
            string_today = str(self.date_today)
            print(string_today > row_date)
    
    def stop_service(self):
        self.__connection.close()