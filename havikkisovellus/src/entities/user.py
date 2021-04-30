"""Class and methods for handling user information."""
class User:
    """Class that holds the user information.

    Attributes:
        username: Username for the user.
        password: Password corresponding to the username.
    """

    def __init__(self, username, password):
        """The constructor for the class.

        Args:
            username: Username for the user.
            password: Password corresponding to the username.
        """
        self._username = username
        self._password = password

    def get_username(self):
        """Return the username for further use.

        Returns:
            The user's username.
        """
        return self._username

    def get_password(self):
        """Return the password for further use.

        Returns:
            The user's password.
        """
        return self._password
