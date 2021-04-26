from tkinter import Tk, ttk, constants, StringVar

from ui_visual.login_view import LoginView
from ui_visual.after_login_view import AfterLoginView

class UI:

    def __init__(self, root, foodservice):
        self._root = root
        self._current_view = None
        self.foodservice = foodservice

    def start(self):
        self._show_login_view()

    def _show_login_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = LoginView(
            self._root,
            self._show_after_login_view,
            self.foodservice
        )

        self._current_view.pack()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_after_marked(self, username, boxes):
        for box in boxes:
            marked, ingr_name = box[0].get(), box[1].get_content()
            if marked == 1:
                self.foodservice.mark_ingredient_as_eaten(username, ingr_name)
        self._show_after_login_view(username)

    def _show_after_login_view(self, username):
        self._hide_current_view()

        ingredients = self.foodservice.list_added_ingredients(username, expire=True)

        self._current_view = AfterLoginView(
            self._root,
            ingredients,
            self._show_after_marked,
            self._show_login_view,
            username
        )

        self._current_view.pack()
