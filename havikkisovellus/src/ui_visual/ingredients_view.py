"""Class and methods for listing the ingredients in the UI."""
from tkinter import ttk, constants, IntVar, StringVar

class IngredientsView:
    """Class for listing the ingredients in the UI.

    Attributes:
        root:
            The root component of the window.
        ingredients:
            List of the ingredients.
        handle_mark_as_eaten:
            The handler function for handling what happens when 'Mark as eaten' is clicked.
        frame:
            The frame to which elements are attached.
        message_var:
            The message to show in the window.
        ingredient_elems:
            Elements created from the ingredients.
    """

    def __init__(self, root, ingredients, handle_mark_as_eaten):
        """The constructor for the class.

        Args:
            root:
                The root component of the window.
            ingredients:
                List of the ingredients.
            handle_mark_as_eaten:
                The handler function for handling what happens when 'Mark as eaten' is clicked.
        """
        self._root = root
        self._ingredients = ingredients
        self._handle_mark_as_eaten = handle_mark_as_eaten

        self._frame = None
        self._message_var = None

        self._ingredient_elems = []

        self._initialize()

    def pack(self):
        """Fill the frame with elements."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroy and delete all the elements in the frame."""
        self._frame.destroy()

    def _create_mark_button(self):
        """Create the 'Mark as eaten' button.
        Return the button only if there are ingredients
        to list.

        Returns: The created button."""
        if self._ingredients:
            mark_button = ttk.Button(
                master=self._frame,
                text="Mark as eaten",
                command=lambda:self._handle_mark_as_eaten(self._ingredient_elems)
            )
            return mark_button
        return None

    def _create_list_header(self):
        """Create the header of the frame.
        Creates
        - the message, and sets a message inside of it
        - and the label for it."""
        self._message_var = StringVar()

        if self._ingredients:
            msg_label_text = "These ingredients will soon become waste.\nPlease eat them soon. :("
            self._message_var.set(msg_label_text)
        else:
            msg_label_text = "Good job!\nYou have no ingredients that will become waste! :)"
            self._message_var.set(msg_label_text)

        msg_label = ttk.Label(master=self._frame, textvariable=self._message_var)
        msg_label.grid(row=0, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _create_list_of_ingredients(self):
        """Create elements of the ingredients and check buttons for them."""
        i = 1
        for ingredient in self._ingredients:
            int_var = IntVar()
            ingr_check_button = ttk.Checkbutton(master=self._frame,
                                               text=ingredient, variable=int_var)
            ingr_check_button.grid(row=i, column=1,
                                  sticky=(constants.E, constants.W),
                                  padx=5, pady=5)
            self._ingredient_elems.append((int_var, ingredient.get_id()))
            i+=1

    def _create_footer(self):
        """Create the 'Mark as eaten' button if needed,
        and position it on the frame."""
        mark_button = self._create_mark_button()
        if mark_button:
            mark_button.grid(column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        """Initialize the frame with the header, the ingredient elements, and the footer."""
        self._frame = ttk.Frame(master=self._root)

        self._create_list_header()
        self._create_list_of_ingredients()
        self._create_footer()
