from book import Fiction, NonFiction
from customer import Customer
from order import Order

fiction_book_list = [
    Fiction('Introduction to Python', 'John Smith', 200),
    Fiction('Data Structure and Algorithms', 'John Doe', 300),
    Fiction('Python Programming', 'John Smith', 300)
]

non_fiction_book_list = [
    NonFiction('Highe Level Design', 'John Smith', 200),
    NonFiction('Low Level Design', 'John Doe', 300),
    NonFiction('Object Orianted Programming', 'John Smith', 300)
]



if __name__ == '__main__':
    while True:
        choice = input('\nChoose a number to select category:\n1. Fiction\n2. Non-Fiction\n3. Exit\n\n')

        if choice == '1':
            print('\n----------Available Fiction Books:----------\n')

            for number, book in enumerate(fiction_book_list, 1):
                print(f'{number}. {book.display_details()}')

            select_index = int(input('\nChoose a number to buy the book: ')) - 1
            selected_book = fiction_book_list[select_index]

            # print(selected_book)

            customer_name = input('Write your name: ')
            customer_email = input('Write your email: ')
            customer_address = input('Write your address: ')

            customer = Customer(customer_name, customer_email, customer_address)

            order = Order(customer)
            order.add_book(selected_book)
            customer.place_order(order)

            print(f"Thank you, {customer_name}! You have placed the following order:")
            print(order)

            break
        
        elif choice == '2':
            print('\n----------Available Non-Fiction Books:----------\n')

            for number, book in enumerate(non_fiction_book_list, 1):
                print(f'{number}. {book.display_details()}')

        elif choice == '3':
            print('\nExiting.............\n')
            break

        else:
            print('\nInvalid choice. Please choose a valid option')
