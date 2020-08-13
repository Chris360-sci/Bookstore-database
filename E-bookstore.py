# Capstone project 1
import sqlite3  # Import sqlite 3
db = sqlite3.connect('ebookstore.db') # Create a database called ebookstore
cursor = db.cursor()  # Get a cursor object
# Drop table (use this if you get a table already exists error)
cursor.execute (''' DROP TABLE books ''')
db.commit()
# Create a table called books
cursor.execute('''
    CREATE TABLE books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT,
                   	Qty INTEGER)
''')
db.commit() # Commit our changes
# List a set of books
books_ = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
    ]
cursor.executemany (''' INSERT INTO books (id, Title, Author, Qty) VALUES(?,?,?,?) ''', books_) # Add the books into the table
db.commit () # Commit our changes
# Define a function to enter a new book into the table
def enter_book():
    "a function that will insert a book into the database" # the id column will autoincrement each time this function is called
    title =  input("enter book title:")
    author = input("enter the author:")
    quantity = input("enter the number of copies of this book:")
    cursor. execute (''' INSERT INTO books(Title, Author, Qty)
    VALUES(?,?,?)''', ( title, author, quantity))
    print(' Entry complete ')
    db.commit()
# Define a function to update any book in the table
def update_book():
    title_ = input('Which book would you like to update?')
    field = input('Would you like to update the title, author or quantity?')
    if field == 'title':
        new_title = input('Please enter the new title:')
        cursor.execute (''' UPDATE books SET Title = ? WHERE Title = ? ''', (new_title, title_))
        db.commit()
    if field == 'author':
        new_author = input('Please enter the new author:')
        cursor.execute (''' UPDATE books SET Author = ? WHERE Title = ? ''', (new_author, title_))
        db.commit()
    if field == 'quantity':
        new_quantity = input('Please enter the new quantity:')
        cursor.execute (''' UPDATE books SET Qty = ? WHERE Title = ? ''', (new_quantity, title_))
        db.commit()
# Define a function to delete a book from the table
def delete_book():
    "this function DROPS a book from the database"
    del_book = input("enter the title of the book to delete:")
    cursor.execute (''' DELETE FROM books WHERE Title = ? ''', (del_book,))
    db.commit()
# Define a function to search for a book from the table    
def search_book():
    "this function will search for a book"
    search_ = input("Would you like to search by author or title?")
    if search_ == 'title':
        search_title = input("Enter the title of the book:")
        cursor.execute (''' SELECT Title, Author, Qty FROM books WHERE Title = ? ''', (search_title,))
        for row in cursor:
            print(' Title: {0}  Author: {1}  Quantity: {2}\n '.format(row[0], row[1], row[2]))
        
    if search_ == 'author':
        search_author = input("enter the author of the book:")
        cursor.execute (''' SELECT Title, Author, Qty FROM books WHERE Author = ? ''', (search_author,))
        for row in cursor:
            print(' Title: {0}  Author: {1}  Quantity: {2}\n '.format(row[0], row[1], row[2]))
        
def view_collection():
    "this function displays info on all books in the table"
    cursor.execute (''' SELECT * FROM books''')
    for row in cursor:
        print(' ID: {0}  Title: {1}  Author: {2}  Quantity: {3}\n '.format(row[0], row[1], row[2], row[3]))
    
running = True

while running: # While the app is running, allow the user to choose what they want to do
    print("What would you like to do?")
    user_choice = input(" \n1. Enter book \n2. Update book \n3. Delete book \n4. Search books \n5. View Collection \n0. Exit \n :")
  
    if user_choice == "1":
        enter_book()
  
    if user_choice == "2":
        update_book()

    if user_choice == "3":
        delete_book()

    if user_choice == "4":
        search_book()

    if user_choice == "5":
        view_collection()

    if user_choice == "0":
        db.close()
        quit()



                 
