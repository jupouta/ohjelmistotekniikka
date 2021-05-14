"""The main file of the program that starts the program."""
from tkinter import Tk

from database.database import Database
from database.initialize_database import initialize_database

from ui_visual.ui import UI
from logic.food_service import FoodService

def main():
    """Main function of the program.
    Start the program from here."""
    initialize_database()

    database = Database()
    foodservice = FoodService(database)

    window = Tk()
    window.title("Food Waste App")

    ui_base = UI(window, foodservice)
    ui_base.start()

    window.mainloop()

if __name__ == '__main__':
    main()
