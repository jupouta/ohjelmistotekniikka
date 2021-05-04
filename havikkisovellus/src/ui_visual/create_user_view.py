from tkinter import ttk, constants, StringVar

class CreateUserView:

    def __init__(self, root, handle_create_user, foodservice):
        self._root = root
        self._handle_create_user = handle_create_user
        self.foodservice = foodservice

        self._frame = None
        self._username = None
        self._password = None
        self._label_var = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user(self):
        username = self._username.get()
        password = self._password.get()

        if self.foodservice.add_user(username, password):
            self._handle_create_user()
        else:
            self._label_var.set('Username already found!')

    def _create_button(self):
        button = ttk.Button(
            master=self._frame,
            text="Create user",
            command=self._create_user
        )
        return button

    def _create_entries(self):
        self._username = ttk.Entry(master=self._frame)
        self._password = ttk.Entry(master=self._frame)
        self._label_var = StringVar()
        self._label_var.set("")

        label = ttk.Label(master=self._frame, text="Create a user:")
        label.grid(row=0, column=0, padx=5, pady=5)

        username_label = ttk.Label(master=self._frame, text="Username")
        username_label.grid(row=1, column=0, padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_label.grid(row=2, column=0, padx=5, pady=5)

        self._username.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._password.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _create_footer(self):
        button = self._create_button()
        button.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        var_label = ttk.Label(master=self._frame, textvariable=self._label_var)
        var_label.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._create_entries()

        self._create_footer()

        self._frame.grid_columnconfigure(1, weight=1, minsize=250)
