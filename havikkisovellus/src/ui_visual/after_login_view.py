"""Class and methods for the user view after logging in."""
import time

from tkinter import ttk, constants, Message, StringVar
from ui_visual.ingredients_view import IngredientsView

class AfterLoginView:
    """Class for the UI view after logging in.

    Attributes:
        root:
            The root component of the window.
        handle_after_logout:
            The method for handling logging out.
        food_service:
            The service class for handling all the logic between the UI and the database.
        ingredient:
            The ingredient field for adding new ingredients.
        date:
            The date field for adding new ingredients.
        frame:
            The frame to which elements are attached.
        ingredients_frame:
            The list of ingredients frame.
        ingredients_view:
            The list of ingredients view to pack and destroy.
        message_var:
            The message entry to show error messages.
    """

    def __init__(self, root, handle_after_logout, food_service):
        """The constructor for the class.

        Args:
            root:
                The root component of the window.
            handle_after_logout:
                The method for handling logging out.
            food_service:
                The service class for handling all the logic between the UI and the database.
        """
        self._root = root
        self._handle_after_logout = handle_after_logout
        self.food_service = food_service

        self._ingredient = None
        self._date = None

        self._frame = None
        self._ingredients_frame = None
        self._ingredients_view = None
        self._message_var = None

        self._initialize()

    def pack(self):
        """Fill the frame with elements."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroy and delete all the elements in the frame."""
        self._frame.destroy()

    def _handle_mark(self, ingredient_elements):
        """Mark the checked ingredients as used,
        and update the view."""
        username = self.food_service.get_user().get_username()

        for ingr_elem in ingredient_elements:
            marked_ingr, ingr_id = ingr_elem[0].get(), ingr_elem[1]
            if marked_ingr == 1:
                self.food_service.mark_ingredient_as_eaten(username, ingr_id)
        self._show_ingredient_list()

    def _show_ingredient_list(self):
        """Update the ingredient elements view."""
        if self._ingredients_view:
            self._ingredients_view.destroy()

        username = self.food_service.get_user().get_username()
        ingredients = self.food_service.list_added_ingredients(username, expire=True)
        self._ingredients_view = IngredientsView(
            self._ingredients_frame,
            ingredients,
            self._handle_mark
        )

        self._ingredients_view.pack()

    def _handle_logout(self):
        """Log out from the service and update the view."""
        self.food_service.log_out()
        self._handle_after_logout()

    def _create_header(self):
        """Create the header elements:
        - message showing who is logged in
        - 'Log out' button."""
        username = self.food_service.get_user().get_username()
        logged_in_label = Message(master=self._frame,text=f"You are logged in, {username}!")
        logged_in_label.grid(row=0, column=1, padx=5, pady=5)

        logout_button = self._create_logout_button()
        logout_button.grid(row=0, column=2, padx=5, pady=5)

    def _create_add_ingredients_elements(self):
        """Create entries for adding ingredients:
        - 'Ingredient' field
        - 'Expire date'  field."""
        i = 3
        ingredient_label = ttk.Label(master=self._frame, text="Ingredient:")
        ingredient_label.grid(row=i, column=0, padx=5, pady=5)
        self._ingredient = ttk.Entry(master=self._frame)
        self._ingredient.grid(row=i, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        date_label = ttk.Label(master=self._frame, text="Expire date:")
        date_label.grid(row=i+1, column=0, padx=5, pady=5)
        self._date = ttk.Entry(master=self._frame)
        self._date.grid(row=i+1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _create_footer(self):
        """Create the footer elements:
        - label for adding ingredients
        - entries for adding ingredients
        - button for adding ingredients
        - error message."""
        add_label_text = ttk.Label(master=self._frame, text="Add a new ingredient below:")
        add_label_text.grid(row=2, column=1, columnspan=2,
                            sticky=(constants.E, constants.W), padx=5, pady=5)

        self._create_add_ingredients_elements()

        add_button = self._create_add_ingredient_button()
        add_button.grid(column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._message_var = StringVar()
        self._message_var.set("")
        msg_var_label = ttk.Label(master=self._frame, textvariable=self._message_var)
        msg_var_label.grid(column=1)

    def _delete_entry_txt_field(self):
        """Delete all the text in the ingredient and date fields."""
        self._ingredient.delete(0, constants.END)
        self._date.delete(0, constants.END)

    def _handle_add_new_ingredient(self):
        """Handle adding a new ingredient. Convert the date into an integer, and
        add the date with today's date and the ingredient name into the database.
        Do not crash if the date is not correct.
        """
        try:
            username = self.food_service.get_user().get_username()
            converted_date = self.food_service.convert_expire_date(self._date.get())
            today = int(time.time())
            self.food_service.add_ingredient(today, self._ingredient.get(),
                                            converted_date, username)

            self._show_ingredient_list()
            self._delete_entry_txt_field()
        except ValueError:
            self._message_var.set("Use the correct form of date: dd/mm/yyyy.")

    def _create_add_ingredient_button(self):
        """Create the 'Add new ingredient' button.
        Returns: The created button."""
        add_button = ttk.Button(
            master=self._frame,
            text="Add new ingredient",
            command=self._handle_add_new_ingredient
            )
        return add_button

    def _create_logout_button(self):
        """Create the 'Logout' button.
        Returns: The created button."""
        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_logout
        )
        return logout_button

    def _initialize(self):
        """Initialize the frame with the header, the ingredient elements, and the footer."""
        self._frame = ttk.Frame(master=self._root)
        self._ingredients_frame = ttk.Frame(master=self._frame)

        self._create_header()
        self._show_ingredient_list()
        self._create_footer()

        self._ingredients_frame.grid(row=1, column=1, columnspan=2)
        self._frame.grid_columnconfigure(1, weight=1, minsize=250)
