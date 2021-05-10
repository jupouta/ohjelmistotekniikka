"""Class and methods for the UI base."""

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
        """The constructor for the class.

        Args:
            root:
                The root component of the window.
            food_service:
                The service class for handling all the logic between the UI and the database."""
        self._root = root
        self._current_view = None
        self.food_service = food_service

    def start(self):
        """Start the UI by showing the login view."""
        self._show_login_view()

    def _show_login_view(self):
        """Create the login view: destroy if already exists, and pack it with elements."""
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
        """Destroy the current view and initialize to None."""
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_create_user_view(self):
        """Create the user creation view: destroy if already exists, and pack it with elements."""
        if self._current_view:
            self._current_view.destroy()

        self._current_view = CreateUserView(
            self._root,
            self._show_login_view,
            self.food_service
        )

        self._current_view.pack()

    def _show_after_login_view(self):
        """Create the after login view: destroy if already exists, and pack it with elements."""
        self._hide_current_view()

        self._current_view = AfterLoginView(
            self._root,
            self._show_login_view,
            self.food_service
        )

        self._current_view.pack()
