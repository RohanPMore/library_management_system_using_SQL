from db.database import Database

def most_borrowed_books():
    db = Database()
    query = '''
    SELECT Books.title, COUNT(Loans.book_id) AS borrow_count
    FROM Loans
    JOIN Books ON Loans.book_id = Books.book_id
    GROUP BY Loans.book_id
    ORDER BY borrow_count DESC
    LIMIT 5
    '''
    results = db.fetch_query(query)
    db.close()
    return results

def overdue_books():
    db = Database()
    query = '''
    SELECT Users.name, Books.title, Loans.loan_date
    FROM Loans
    JOIN Users ON Loans.user_id = Users.user_id
    JOIN Books ON Loans.book_id = Books.book_id
    WHERE return_date IS NULL AND loan_date < date('now', '-30 day')
    '''
    results = db.fetch_query(query)
    db.close()
    return results
