class Book:
    def __init__(self, title, author, price, stock_quantity):
        self.title = title
        self.author = author
        self.price = price
        self.stock_quantity = stock_quantity

    def update_quantity(self, quantity):
        self.stock_quantity += quantity

        return self.stock_quantity
    
    def __str__(self):
        # return f'Book Name: {self.title} by {self.author}, Price: {self.price}, Total Quantity: {self.stock_quantity}'
        return f'{self.title} by {self.author}'


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

# book object
book1 = Book('Introduction to Python', 'Eusuf Ahamed', 200, 20)
book1.update_quantity(20)
print('Book Object: ', book1)

# customer object
customer1 = Customer('Eusuf Ahamed', 'eusufahmed789@gmail.com', 'Dhake')
print('Customer Name: ', customer1)

# order object
order1 = Order(customer1)
order1.add_book(book1)
customer1.place_order(order1)

customer_books = customer1.get_all_books()
print(f'{customer1} has bought the following books')
for book in customer_books:
    print('Book Name: ', book)

