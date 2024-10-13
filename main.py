from modules.books import add_book, search_books, delete_book
from modules.users import add_user, borrow_book, return_book
from modules.reports import most_borrowed_books, overdue_books

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Search Books")
    print("3. Delete Book")
    print("4. Add User")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Most Borrowed Books")
    print("8. Overdue Books")
    print("9. Exit")

def main():
    while True:
        main_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter year published: "))
            genre = input("Enter genre: ")
            copies = int(input("Enter number of copies: "))
            add_book(title, author, year, genre, copies)

        elif choice == '2':
            keyword = input("Enter search keyword: ")
            books = search_books(keyword)
            if books:
                for book in books:
                    print(f"{book[0]} | {book[1]} | {book[2]}")
            else:
                print("No books found.")

        elif choice == '3':
            book_id = int(input("Enter book ID to delete: "))
            delete_book(book_id)

        elif choice == '4':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            add_user(name, email)

        elif choice == '5':
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            borrow_book(user_id, book_id)

        elif choice == '6':
            loan_id = int(input("Enter loan ID: "))
            return_book(loan_id)

        elif choice == '7':
            books = most_borrowed_books()
            for book in books:
                print(f"{book[0]} | Borrowed {book[1]} times")

        elif choice == '8':
            overdue = overdue_books()
            for record in overdue:
                print(f"{record[0]} | {record[1]} | Loaned on {record[2]}")

        elif choice == '9':
            print("Exiting system...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
