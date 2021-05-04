import time

from ui_visual.login_view import LoginView
from ui_visual.create_user_view import CreateUserView
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
            self._show_create_user_view,
            self.foodservice
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
            self.foodservice
        )

        self._current_view.pack()

    def _show_after_login_view(self):
        self._hide_current_view()

        self._current_view = AfterLoginView(
            self._root,
            self._show_login_view,
            self._show_after_new_added,
            self.foodservice
        )

        self._current_view.pack()

    def _show_after_new_added(self, ingredient, date, username):
        converted_date = self.foodservice.convert_expire_date(date)
        today = int(time.time())
        self.foodservice.add_ingredient(today, ingredient, converted_date, username)

        self._show_after_login_view()
