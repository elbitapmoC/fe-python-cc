import uuid

# Online Book System (OOP)
# Similiar to Amazon Kindle (for Short shorties)
'''
Library
  - Can add/remove:
    - User (Can checkout/return a book from the library)
      - id (int)
      - name (string)
      - dob (datetime)
    - Book
      - id (int)
      - title (string)
      - content (list)
        - One page of text at a time in the active book.
      - current_page (int)
        - Remembers last page read
      - in_stock (bool)
    - Library
      - checkout_date (datetime)
      - due_date (datetime)
      - user_id (int)
      - book_id (int)
      - Books
      - Users
'''


class Book:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.current_page = 0
        self.in_stock = true
        self.content = content

    def next_pg(self):
        self.current_page += 1
        return content[self.current_page]

    def previous_pg(self):
        self.current_page -= 1
        return content[self.current_page]

    def get_title(self):
        return self.title

    def get_id(self):
        return self.id

    def get_pg(self):
        return self.current_page


class User:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


class Library:
    def __init__(self):
        self.collection = dict()
        self.users = dict()
        self.checkedout_books = []

    def checkout_book(self, book_id):
        # due set at checkout
        # user_id and book_id passed in to keep track.
        self.collection.book_id
        print('Book has been checked out! Enjoy!')

    def check_availability(self, book_id):
        if book_id in checkedout_books:
            print('Someone is currently using this book. Try again next week!')
        else:
            checkout(book_id)

    def return_book(self, book_id):
        self.checkedout_books.remove(book_id)
        print('Book has been returned, we hope you liked what you read!')

    def add_book_to_library(self, title, content):
        new_book = Book(uuid.uuid1, title, content)
        self.collection[new_book.id] = new_book

    def add_user_to_library(self, name, dob):
        new_user = User(uuid.uuid1, name, dob)
        self.users[new_book.id] = new_book
