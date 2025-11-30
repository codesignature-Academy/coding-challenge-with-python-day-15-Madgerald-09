class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    def borrow(self, book):
        if book.is_borrowed:
            print(f"'{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"'{self.name}' borrowed '{book.title}'")
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"'{self.name}' returned '{book.title}'")
        else:
            print(f"'{self.name}' did not borrow '{book.title}'.")
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")
    def register_member(self, member):
        self.members.append(member)
        print(f"Registered Member: {member.name} (ID: {member.member_id})")
    def show_available_books(self):
        print("Available Books:")
        for book in self.books:
            if not book.is_borrowed:
                print(book)
library = Library()
book1 = Book("How to make 300k by sleeping", "Madgerald D Great", "001 for Africa")
book2 = Book("How to escape from bandits in Nigeria", "Yusuf the Rascal", "102")
book3 = Book("How to sub 86gb with 100naira", "MTN Coperatives", "234")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
member1 = Member("Gerald", "M001")
member2 = Member("Chinemerem", "M002")
library.register_member(member1)
library.register_member(member2)
# print(Book)
