"""Class and methods for creating a user in the UI."""
from tkinter import ttk, constants, StringVar

class CreateUserView:
    """Class for listing the ingredients in the UI.

    Attributes:
        root:
            The root component of the window.
        handle_create_user:
            The method for refreshing the view when a new user is created.
        food_service:
            The service class for handling all the logic between the UI and the database.
        frame:
            The frame to which elements are attached.
        message_var:
            The message to show in the window.
        username:
            The username field for creating a user.
        password:
            The password field for creaging a user.
    """

    def __init__(self, root, handle_create_user, food_service):
        """The constructor for the class.

        Args:
            root:
                The root component of the window.
            handle_create_user:
                The method for refreshing the view when a new user is created.
            food_service:
                The service class for handling all the logic between the UI and the database."""
        self._root = root
        self._handle_create_user = handle_create_user
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

    def _create_user(self):
        """Create a user with the given username and password.
        If username is already taken, show an error message."""
        username = self._username.get()
        password = self._password.get()

        if self.food_service.add_user(username, password):
            self._handle_create_user()
        else:
            self._message_var.set('Username already found!')

    def _create_user_button(self):
        """Create the 'Create user' button.
        Returns: The created button."""
        create_button = ttk.Button(
            master=self._frame,
            text="Create user",
            command=self._create_user
        )
        return create_button

    def _create_header(self):
        """Create elements for creating a user.
        - entries for username and password
        - error message
        - labels for the entries."""
        self._username = ttk.Entry(master=self._frame)
        self._password = ttk.Entry(master=self._frame)
        self._message_var = StringVar()
        self._message_var.set("")

        create_label = ttk.Label(master=self._frame, text="Create a user:")
        create_label.grid(row=0, column=0, padx=5, pady=5)

        username_label = ttk.Label(master=self._frame, text="Username")
        username_label.grid(row=1, column=0, padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_label.grid(row=2, column=0, padx=5, pady=5)

        self._username.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._password.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _create_footer(self):
        """Create the footer of the view:
        - button for adding the user
        - error message label."""
        user_button = self._create_user_button()
        user_button.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        msg_var_label = ttk.Label(master=self._frame, textvariable=self._message_var)
        msg_var_label.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        """Initialize the frame with the header, and the footer."""
        self._frame = ttk.Frame(master=self._root)

        self._create_header()
        self._create_footer()

        self._frame.grid_columnconfigure(1, weight=1, minsize=250)
