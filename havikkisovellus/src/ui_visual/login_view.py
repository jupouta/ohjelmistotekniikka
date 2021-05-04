from tkinter import ttk, constants, StringVar


class LoginView:
    def __init__(self, root, show_login, show_create_user, foodservice):
        self._root = root
        self._show_login = show_login
        self._show_create_user = show_create_user
        self._frame = None
        self._label_var = None

        self.foodservice = foodservice

        self._username = None
        self._password = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_login(self):
        username = self._username.get()
        password = self._password.get()

        accepted = self.foodservice.check_username(username, password)
        if accepted:
            self._label_var.set("Login accepted!")
            self._show_login()
        else:
            self._label_var.set("Userword or password not found!")

    def _create_login_entries(self):
        self._username = ttk.Entry(master=self._frame)
        self._password = ttk.Entry(master=self._frame)
        self._label_var = StringVar()
        self._label_var.set("")

        label = ttk.Label(master=self._frame, text="Login:")
        label.grid(row=0, column=0, padx=5, pady=5)

        username_label = ttk.Label(master=self._frame, text="Username")
        username_label.grid(row=1, column=0, padx=5, pady=5)

        self._username.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._password.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_label.grid(row=2, column=0, padx=5, pady=5)

    def _create_enter_button(self):
        button = ttk.Button(
            master=self._frame,
            text="Enter login",
            command=self._handle_login
        )
        return button

    def _create_button_user(self):
        button = ttk.Button(
            master=self._frame,
            text="Create user",
            command=self._show_create_user
        )
        return button

    def _create_buttons(self):
        button = self._create_enter_button()
        button.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        var_label = ttk.Label(master=self._frame, textvariable=self._label_var)
        var_label.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        create_button = self._create_button_user()
        create_button.grid(row=5, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._create_login_entries()

        self._create_buttons()

        self._frame.grid_columnconfigure(1, weight=1, minsize=250)
