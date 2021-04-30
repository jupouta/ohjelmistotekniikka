"""Class and methods for handling ingredient information."""
from datetime import date

class Ingredient:
    """Class that holds the ingredient information.

    Attributes:
        content: Ingredient's name.
        date_added: The date the ingredient was added to the database.
        date_preserves: The date the ingredient will expire.
        used: If the ingredient is used already.
    """

    def __init__(self, content, date_added, date_expires, used=0):
        """The constructor for the class.

        Args:
            content:
                Ingredient's name.
            date_added:
                The date the ingredient was added to the database.
            date_preserves:
                The date the ingredient will expire.
            used:
                Optional; If the ingredient is used already.
                If not given, not used (0) is assumed.
        """
        self.content = content
        self.date_added = self.convert_date(date_added)
        self.date_expires = self.convert_date(date_expires)
        self.used = self.convert_used(used)

    def convert_date(self, date_given):
        """Converts the given date from the timestamp format
        to a more human readable format, e.g. '2021-05-01'.

        Args:
            date_given: The date to be converted in timestamp format (int).

        Returns:
            The converted date."""
        return date.fromtimestamp(date_given)

    def convert_used(self, used_given):
        """Converts the given int into a boolean value.

        Args:
            used_given:
                The int value representing if the ingredient is used.
                I.e. 1 is True, 0 is False.

        Returns:
            Boolean value that corresponds to the given int value."""

        if used_given == 1:
            return True
        return False

    def is_close_to_perishing(self):
        """Counts the days between today and the expire date and returns the
        boolean value if the ingredient is less than 5 days away from perishing.

        Returns:
            Boolean value: if there are less than 5 days between today
            and the ingredient perishing."""
        difference_in_days = (self.date_expires - date.today()).days
        if difference_in_days < 5:
            return True
        return False

    def is_used(self):
        """Return 'used'.

        Returns: The attribute 'used' for further use."""
        return self.used

    def get_content(self):
        """Return 'content'.

        Returns: The attribute 'content' for further use."""
        return self.content

    def __str__(self):
        """Forms a string format of the ingredient.

        Returns: A string with the attributes 'content', 'date_added',
        'date_expires', and 'used'."""
        eaten = ''
        if self.used:
            eaten = ', already eaten'
        else:
            eaten = ', not eaten yet'
        to_print = f'{self.content}: added {self.date_added}, expires {self.date_expires}{eaten}'
        return to_print
