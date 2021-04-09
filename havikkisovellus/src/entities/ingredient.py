from datetime import date
class Ingredient:
    
    def __init__(self, content, date_added, preserves=False):
        self.content = content
        self.date_added = self.convert_date(date_added)
        self.preserves = preserves
    
    def convert_date(self, date_given):
        return date.fromtimestamp(date_given)
    
    def is_close_to_perishing(self):
        difference_in_days = (date.today() - self.date_added).days
        if difference_in_days > 5:
            return True
        return False
    
    def __str__(self):
        if self.preserves:
            return f'{self.content}: added {self.date_added}'
        else:
            return f'{self.content}: added {self.date_added}'