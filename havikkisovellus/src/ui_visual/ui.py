from tkinter import Tk, ttk, constants

class UI:

    def __init__(self, root, foodservice):
        self._root = root
        self._username = None
        self._password = None

        self.foodservice = foodservice

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Login")

        self._username = ttk.Entry(master=self._root)
        username_label = ttk.Label(master=self._root, text="Username")

        self._password = ttk.Entry(master=self._root)
        password_label = ttk.Label(master=self._root, text="Password")

        button = ttk.Button(
          master=self._root,
          text="Enter",
          command=self._handle_button_click
        )
        heading_label.grid(row=0, column=0, padx=5, pady=5)

        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username.grid(row=1, column=1, padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password.grid(row=2, column=1, padx=5, pady=5)

        button.grid(row=3, column=1, padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=250)

    def _handle_button_click(self):
        username_value = self._username.get()
        password_value = self._password.get()

        print(f"Username: {username_value}, Password: {password_value}")

        accepted = self.foodservice.check_username(username_value, password_value)
        if accepted:
            print('Login accepted!')

