from db.database import Database

def add_book(title, author, published_year, genre, copies_available):
    db = Database()
    query = '''
    INSERT INTO Books (title, author, published_year, genre, copies_available)
    VALUES (?, ?, ?, ?, ?)
    '''
    db.execute_query(query, (title, author, published_year, genre, copies_available))
    db.close()
    print(f"Book '{title}' added successfully!")

def search_books(keyword):
    db = Database()
    query = '''
    SELECT * FROM Books WHERE title LIKE ? OR author LIKE ? OR genre LIKE ?
    '''
    books = db.fetch_query(query, (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
    db.close()
    return books

def delete_book(book_id):
    db = Database()
    query = 'DELETE FROM Books WHERE book_id = ?'
    db.execute_query(query, (book_id,))
    db.close()
    print(f"Book ID {book_id} deleted successfully!")
