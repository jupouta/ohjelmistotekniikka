import tkinter

from ui.ui import UI

from database.database import Database
from database.initialize_database import initialize_database

from logic.food_service import FoodService

def main():
    initialize_database()

    database = Database()
    foodservice = FoodService(database)

    new_ui = UI(foodservice)
    new_ui.start()

if __name__ == '__main__':
    main()
