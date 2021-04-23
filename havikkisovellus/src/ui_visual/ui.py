from tkinter import Tk, ttk, constants, StringVar

from ui_visual.login_view import LoginView
from ui_visual.after_login_view import AfterLoginView

class UI:

    def __init__(self, root, foodservice):
        self._root = root
        self._current_view = None

        self._username = None
        self._password = None

        self.foodservice = foodservice

    def start(self):
        self._show_login_view()

    def _show_login_view(self):
        self._current_view = LoginView(
            self._root,
            self._handle_login,
            self.foodservice
        )

        self._current_view.pack()

    def _handle_login(self, username):
        self._show_after_login_view(username)

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    # TODO
    def _show_after_marked(self, username, boxes):
        for box in boxes:
            print(box.get())
        self._show_after_login_view(username)

    def _show_after_login_view(self, username):
        self._hide_current_view()

        ingredients = self.foodservice.list_added_ingredients(username, expire=True)

        self._current_view = AfterLoginView(
            self._root,
            ingredients,
            self._show_after_marked,
            username
        )

        self._current_view.pack()
