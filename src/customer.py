class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.orders = []
    
    def place_order(self, order):
        self.orders.append(order)

    def get_all_books(self):
        all_books = []
        for order in self.orders:
            all_books.extend(order.books)
        return all_books

    def __str__(self):
        return self.name