"""Class and methods for the login view."""
from tkinter import ttk, constants, StringVar


class LoginView:
    """Class for the UI view for logging in.

    Attributes:
        root:
            The root component of the window.
        show_after_login:
            The method for showing the after login view.
        show_create_user:
            The method for showing the user creation view.
        food_service:
            The service class for handling all the logic between the UI and the database.
        frame:
            The frame to which elements are attached.
        message_var:
            The message entry to show error messages.
        username:
            The username field for logging the user in.
        password:
            The password field for logging the user in."""
    def __init__(self, root, show_after_login, show_create_user, food_service):
        """The constructor for the class.

        Args:
            root:
                The root component of the window.
            show_after_login:
                The method for showing the after login view.
            show_create_user:
                The method for showing the user creation view.
            food_service:
                The service class for handling all the logic between the UI and the database."""
        self._root = root
        self._show_after_login = show_after_login
        self._show_create_user = show_create_user
        self.food_service = food_service

        self._frame = None
        self._message_var = None

        self._username = None
        self._password = None

        self._initialize()

    def pack(self):
        """Fill the frame with elements."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroy and delete all the elements in the frame."""
        self._frame.destroy()

    def _handle_login(self):
        """Handle the logging in.
        Check that the username and password are correct.
        If not, set the error message."""
        username = self._username.get()
        password = self._password.get()

        accepted = self.food_service.check_username(username, password)
        if accepted:
            self._message_var.set("Login accepted!")
            self._show_after_login()
        else:
            self._message_var.set("Userword or password not found!")

    def _create_login_entries(self):
        """Create the username and password entries."""
        self._username = ttk.Entry(master=self._frame)
        self._password = ttk.Entry(master=self._frame)
        self._message_var = StringVar()
        self._message_var.set("")

        label = ttk.Label(master=self._frame, text="Login:")
        label.grid(row=0, column=0, padx=5, pady=5)

        username_label = ttk.Label(master=self._frame, text="Username")
        username_label.grid(row=1, column=0, padx=5, pady=5)

        self._username.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._password.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_label.grid(row=2, column=0, padx=5, pady=5)

    def _create_enter_button(self):
        """Create the 'Enter login' button.
        Returns: The created button."""
        button = ttk.Button(
            master=self._frame,
            text="Enter login",
            command=self._handle_login
        )
        return button

    def _create_button_user(self):
        """Create the 'Create user' button.
        Returns: The created button."""
        button = ttk.Button(
            master=self._frame,
            text="Create user",
            command=self._show_create_user
        )
        return button

    def _create_buttons(self):
        """Create the needed buttons and their labels."""
        button = self._create_enter_button()
        button.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        var_label = ttk.Label(master=self._frame, textvariable=self._message_var)
        var_label.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        create_button = self._create_button_user()
        create_button.grid(row=5, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        """Initialize the frame with the login entries, and the buttons."""
        self._frame = ttk.Frame(master=self._root)

        self._create_login_entries()

        self._create_buttons()

        self._frame.grid_columnconfigure(1, weight=1, minsize=250)
