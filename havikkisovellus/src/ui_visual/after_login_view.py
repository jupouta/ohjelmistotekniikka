from ui_visual.ingredients_view import IngredientsView
from tkinter import ttk, constants, Message, IntVar, StringVar

class AfterLoginView:

    def __init__(self, root, handle_after_logout,
                 handle_add_new, foodservice):
        self._root = root
        self._handle_after_logout = handle_after_logout
        self._handle_add_new = handle_add_new

        self.foodservice = foodservice
        self._username = self.foodservice.get_user().get_username()
        self._ingredients = self.foodservice.list_added_ingredients(self._username, expire=True)

        self._ingredient = None
        self._date = None

        self._frame = None
        self._ingredient_frame = None
        self._ingredients_view = None
        self._label_var = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_mark(self, boxes):
        for box in boxes:
            marked, ingr_name = box[0].get(), box[1].get_content()
            if marked == 1:
                self.foodservice.mark_ingredient_as_eaten(self._username, ingr_name)
        self._show_ingredient_list()

    def _show_ingredient_list(self):
        if self._ingredients_view:
            self._ingredients_view.destroy()

        self._ingredients = self.foodservice.list_added_ingredients(self._username, expire=True)
        self._ingredients_view = IngredientsView(
            self._ingredient_frame,
            self._ingredients,
            self._handle_mark
        )

        self._ingredients_view.pack()

    def _handle_logout(self):
        self.foodservice.log_out()
        self._handle_after_logout()

    def _create_header(self):
        label = Message(master=self._frame, text=f"You are logged in, {self._username}!")
        label.grid(row=0, column=1, padx=5, pady=5)

        logout_button = self._create_logout_button()
        logout_button.grid(row=0, column=2, padx=5, pady=5)

    def _create_add_entries(self):
        i = 3
        add_label = ttk.Label(master=self._frame, text="Ingredient:")
        add_label.grid(row=i, column=0, padx=5, pady=5)
        self._ingredient = ttk.Entry(master=self._frame)
        self._ingredient.grid(row=i, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        date_label = ttk.Label(master=self._frame, text="Expire date:")
        date_label.grid(row=i+1, column=0, padx=5, pady=5)
        self._date = ttk.Entry(master=self._frame)
        self._date.grid(row=i+1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _create_footer(self):
        add_label_text = ttk.Label(master=self._frame, text="Add a new ingredient below")
        add_label_text.grid(row=2, column=1, columnspan=2,
                            sticky=(constants.E, constants.W), padx=5, pady=5)

        self._create_add_entries()

        add_button = self._create_add_ingredient_button()
        add_button.grid(column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _create_add_ingredient_button(self):
        button = ttk.Button(
            master=self._frame,
            text="Add new ingredient",
            command=lambda:self._handle_add_new(
                self._ingredient.get(), self._date.get(), self._username)
        )
        return button

    def _create_logout_button(self):
        button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_logout
        )
        return button

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._ingredient_frame = ttk.Frame(master=self._frame)

        self._create_header()
        self._show_ingredient_list()
        self._create_footer()

        self._ingredient_frame.grid(row=1, column=1, columnspan=2)
        self._frame.grid_columnconfigure(1, weight=1, minsize=250)
