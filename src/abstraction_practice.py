from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @abstractmethod
    def display_details(self):
        pass


class Fiction(Book):
    def __init__(self, title, author, price, genre):
        super().__init__(title, author, price)
        self.genre = genre

    def display_details(self):
        print(f'Fiction Book: {self.title} by {self.author}')
        print(f'Genre: {self.genre}')
        print(f'Price: {self.price}')

class NonFiction(Book):
    def __init__(self, title, author, price, topic):
        super().__init__(title, author, price)
        self.topic = topic

    def display_details(self):
        print(f'Non-Fiction Book: {self.title} by {self.author}')
        print(f'Topic: {self.topic}')
        print(f'Price: {self.price}')

fiction1 = Fiction('Python Programming', 'Eusuf Ahamed', 300, 'Romance')
fiction1.display_details()