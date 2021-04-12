from ui.ui import UI
from database import Database
from logic.food_service import FoodService

from initialize_database import initialize_database
import tkinter

def main():
    initialize_database()
    database = Database()
    foodservice = FoodService(database)

    new_ui = UI(foodservice)
    new_ui.start()

if __name__ == '__main__':
    main()