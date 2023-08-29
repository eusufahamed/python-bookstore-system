class Order:
    def __init__(self, customer):
        self.customer = customer
        self.books = []
        self.total_price = 0

    def add_book(self, book):
        self.books.append(book)
        self.total_price =+ book.price

    def __str__(self):
        return f'Order for {self.customer}, Total Price: {self.total_price}'