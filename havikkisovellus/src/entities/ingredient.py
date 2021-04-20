from datetime import date
class Ingredient:

    def __init__(self, content, date_added, date_preserves, used=0):
        self.content = content
        self.date_added = self.convert_date(date_added)
        self.date_preserves = self.convert_date(date_preserves)
        self.used = used

    def convert_date(self, date_given):
        return date.fromtimestamp(date_given)

    def convert_used(self, used_given):
        if used_given == 1:
            return True
        return False

    def is_close_to_perishing(self):
        difference_in_days = (self.date_preserves - date.today()).days
        if difference_in_days < 5:
            return True
        return False

    def is_used(self):
        return self.convert_used(self.used)

    def mark_as_used(self):
        self.used = True

    def __str__(self):
        if self.used == 1:
            print_string = f'''{self.content}: added {self.date_added}, expires {self.date_preserves}, already eaten'''
        else:
            print_string = f'''{self.content}: added {self.date_added}, expires {self.date_preserves}, not eaten yet'''
        return print_string
