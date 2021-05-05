from tkinter import ttk, constants, Message
from ui_visual.ingredients_view import IngredientsView

class AfterLoginView:

    def __init__(self, root, handle_after_logout,
                 handle_add_new_ingredient, food_service):
        self._root = root
        self._handle_after_logout = handle_after_logout
        self._handle_add_new_ingredient = handle_add_new_ingredient

        self.food_service = food_service
        self._username = self.food_service.get_user().get_username()
        self._ingredients = self.food_service.list_added_ingredients(self._username, expire=True)

        self._ingredient = None
        self._date = None

        self._frame = None
        self._ingredients_frame = None
        self._ingredients_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_mark(self, ingredient_elements):
        for ingr_elem in ingredient_elements:
            marked_ingr, ingr_id = ingr_elem[0].get(), ingr_elem[1]
            if marked_ingr == 1:
                self.food_service.mark_ingredient_as_eaten(self._username, ingr_id)
        self._show_ingredient_list()

    def _show_ingredient_list(self):
        if self._ingredients_view:
            self._ingredients_view.destroy()

        self._ingredients = self.food_service.list_added_ingredients(self._username, expire=True)
        self._ingredients_view = IngredientsView(
            self._ingredients_frame,
            self._ingredients,
            self._handle_mark
        )

        self._ingredients_view.pack()

    def _handle_logout(self):
        self.food_service.log_out()
        self._handle_after_logout()

    def _create_header(self):
        logged_in_label = Message(master=self._frame,text=f"You are logged in, {self._username}!")
        logged_in_label.grid(row=0, column=1, padx=5, pady=5)

        logout_button = self._create_logout_button()
        logout_button.grid(row=0, column=2, padx=5, pady=5)

    def _create_add_ingredients_elements(self):
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
        add_label_text = ttk.Label(master=self._frame, text="Add a new ingredient below:")
        add_label_text.grid(row=2, column=1, columnspan=2,
                            sticky=(constants.E, constants.W), padx=5, pady=5)

        self._create_add_ingredients_elements()

        add_button = self._create_add_ingredient_button()
        add_button.grid(column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _create_add_ingredient_button(self):
        add_button = ttk.Button(
            master=self._frame,
            text="Add new ingredient",
            command=lambda:self._handle_add_new_ingredient(
                self._ingredient.get(),
                self._date.get(),
                self._username)
        )
        return add_button

    def _create_logout_button(self):
        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_logout
        )
        return logout_button

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._ingredients_frame = ttk.Frame(master=self._frame)

        self._create_header()
        self._show_ingredient_list()
        self._create_footer()

        self._ingredients_frame.grid(row=1, column=1, columnspan=2)
        self._frame.grid_columnconfigure(1, weight=1, minsize=250)
