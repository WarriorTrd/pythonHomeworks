class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def __repr__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(
                f"{self.name} cann't borrow more than 3 books."
            )
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(
                f"The book '{book.title}' is already borrowed."
            )

        book.is_borrowed = True
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

    def __repr__(self):
        return f"Member: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_books(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")

        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(f"The book '{book_title}' does not exist in the library.")

        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")

        book = next((b for b in member.borrowed_books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(f"The book '{book_title}' does not exist in the library.")

        member.return_book(book)
    
    def __repr__(self):
        return f"Library Books: {self.books}\nMembers: {self.members}"

if __name__ == "__main__":
    library = Library()

    library.add_books(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_books(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_books(Book("Rich dad and poor dad", "robert kiyosaki"))
    library.add_books(Book("Harry Potter", "J.K. Rowling"))
    library.add_books(Book("Sherlock Holmes", "Arthur Conane Doyle"))
    library.add_books(Book("Metro", "Dostaevskiy"))
    library.add_books(Book("Chinor", "Abdulla Qodiriy"))
    library.add_books(Book("Guliver", "Jonathan Swift"))
    library.add_books(Book("Little Prince", "Antoine de Saint-Exupéry"))
    library.add_books(Book("War and Peace", "Leo Tolstoy"))
    library.add_books(Book("1984", "George Orwell"))
    

    library.add_member(Member("Sam"))
    library.add_member(Member("Bob"))

    try:
        library.borrow_book("Sam", "Guliver")
        library.borrow_book("Sam", "1984")
        library.borrow_book("Sam", "War and Peace")
        
        library.borrow_book("Sam", "Harry Potter")
    except Exception as e:
        print(e)

    try:
        
        library.borrow_book("Sam", "Sherlock Holmes")
    except Exception as e:
        print(e)

   
    try:
        library.return_book("Sam", "Guliver")
    except Exception as e:
        print(e)

   
    print(library)