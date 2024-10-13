from db.database import Database
from datetime import datetime

def add_user(name, email):
    db = Database()
    query = '''
    INSERT INTO Users (name, email, join_date)
    VALUES (?, ?, ?)
    '''
    join_date = datetime.now().strftime('%Y-%m-%d')
    db.execute_query(query, (name, email, join_date))
    db.close()
    print(f"User '{name}' added successfully!")

def borrow_book(user_id, book_id):
    db = Database()

    # Check if the book is available
    check_query = 'SELECT copies_available FROM Books WHERE book_id = ?'
    copies = db.fetch_query(check_query, (book_id,))
    
    if copies[0][0] > 0:
        # Borrow the book
        loan_date = datetime.now().strftime('%Y-%m-%d')
        query = '''
        INSERT INTO Loans (user_id, book_id, loan_date)
        VALUES (?, ?, ?)
        '''
        db.execute_query(query, (user_id, book_id, loan_date))

        # Update the available copies
        update_query = 'UPDATE Books SET copies_available = copies_available - 1 WHERE book_id = ?'
        db.execute_query(update_query, (book_id,))
        print("Book borrowed successfully!")
    else:
        print("Book is not available!")

    db.close()

def return_book(loan_id):
    db = Database()

    # Check the loan details
    check_query = 'SELECT book_id FROM Loans WHERE loan_id = ?'
    book_id = db.fetch_query(check_query, (loan_id,))

    if book_id:
        # Return the book
        return_date = datetime.now().strftime('%Y-%m-%d')
        query = 'UPDATE Loans SET return_date = ? WHERE loan_id = ?'
        db.execute_query(query, (return_date, loan_id))

        # Update the available copies
        update_query = 'UPDATE Books SET copies_available = copies_available + 1 WHERE book_id = ?'
        db.execute_query(update_query, (book_id[0][0],))

        print("Book returned successfully!")
    else:
        print("Invalid loan ID!")

    db.close()
