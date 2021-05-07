"""Class and methods for the UI base."""

import time

from ui_visual.login_view import LoginView
from ui_visual.create_user_view import CreateUserView
from ui_visual.after_login_view import AfterLoginView

class UI:
    """Class for the UI and its base.

    Attributes:
        root:
            The root component of the window.
        current_view:
            The current frame in the window.
        food_service:
            The service class for handling all the logic between the UI and the database.
    """

    def __init__(self, root, food_service):
        self._root = root
        self._current_view = None
        self.food_service = food_service

    def start(self):
        self._show_login_view()

    def _show_login_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = LoginView(
            self._root,
            self._show_after_login_view,
            self._show_create_user_view,
            self.food_service
        )

        self._current_view.pack()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_create_user_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = CreateUserView(
            self._root,
            self._show_login_view,
            self.food_service
        )

        self._current_view.pack()

    def _show_after_login_view(self):
        self._hide_current_view()

        self._current_view = AfterLoginView(
            self._root,
            self._show_login_view,
            self._show_after_new_added,
            self.food_service
        )

        self._current_view.pack()

    # TODO: after_login
    def _show_after_new_added(self, ingredient, date, username):
        converted_date = self.food_service.convert_expire_date(date)
        today = int(time.time())
        try:
            self.food_service.add_ingredient(today, ingredient, converted_date, username)
        except ValueError:
            print('value not correct')

        self._show_after_login_view()
