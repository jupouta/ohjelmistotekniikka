from tkinter import Tk

#from ui.ui import UI
from ui_visual.ui import UI

from database.database import Database
from database.initialize_database import initialize_database

from logic.food_service import FoodService

def main():
    initialize_database()

    database = Database()
    foodservice = FoodService(database)

    window = Tk()
    window.title("Food Waste App")

    ui = UI(window, foodservice)
    ui.start()

    window.mainloop()

    #new_ui = UI(foodservice)
    #new_ui.start()

if __name__ == '__main__':
    main()
