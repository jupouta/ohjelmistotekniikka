from datetime import date
class Ingredient:

    def __init__(self, content, date_added, date_preserves):
        self.content = content
        self.date_added = self.convert_date(date_added)
        self.date_preserves = self.convert_date(date_preserves)

    def convert_date(self, date_given):
        return date.fromtimestamp(date_given)

    def is_close_to_perishing(self):
        difference_in_days = (self.date_preserves - date.today()).days
        if difference_in_days < 5:
            return True
        return False

    def __str__(self):
        return f'{self.content}: added {self.date_added}, expires {self.date_preserves}'
