from book import Fiction, NonFiction

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

            # choice = input('\nChoose a number to buy book:\n1. \n2. \n3\n\n')
        
        elif choice == '2':
            print('\n----------Available Non-Fiction Books:----------\n')

            for number, book in enumerate(non_fiction_book_list, 1):
                print(f'{number}. {book.display_details()}')

        elif choice == '3':
            print('\nExiting.............\n')
            break

        else:
            print('\nInvalid choice. Please choose a valid option')
