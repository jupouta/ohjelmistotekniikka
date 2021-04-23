from tkinter import ttk, constants, StringVar


class LoginView:
    def __init__(self, root, handle_login, foodservice):
        self._root = root
        self._handle_login = handle_login
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

    def _show_login_handler(self):
        username = self._username.get()
        password = self._password.get()

        accepted = self.foodservice.check_username(username, password)
        if accepted:
            self._label_var.set("Login accepted!")
            self._handle_login(username)
        else:
            self._label_var.set("Userword or password not found!")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Login:")

        self._username = ttk.Entry(master=self._frame)
        username_label = ttk.Label(master=self._frame, text="Username")

        self._password = ttk.Entry(master=self._frame)
        password_label = ttk.Label(master=self._frame, text="Password")

        button = ttk.Button(
            master=self._frame,
            text="Enter login",
            command=self._show_login_handler
        )

        self._label_var = StringVar()
        self._label_var.set("")

        var_label = ttk.Label(master=self._frame, textvariable=self._label_var)

        label.grid(row=0, column=0, padx=5, pady=5)

        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        button.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        var_label.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=250)
