from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @abstractmethod
    def display_details(self):
        pass