from ui.ui import UI
from initialize_database import initialize_database

def main():
    initialize_database()

    new_ui = UI()
    new_ui.start()

if __name__ == '__main__':
    main()