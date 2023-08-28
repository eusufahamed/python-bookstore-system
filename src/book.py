from book_abstract import Book

class Fiction(Book):
    def display_details(self):
        return f'{self.title} by {self.author}, Price: {self.price}'
    
    def __str__(self):
        return f'{self.title} by {self.author}'
    
class NonFiction(Book):
    def display_details(self):
        return f'{self.title} by {self.author}, Price: {self.price}'
    
    def __str__(self):
        return f'{self.title} by {self.author}'