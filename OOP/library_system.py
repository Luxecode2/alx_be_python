# oop/library_system.py

class Book:
    def __init__(self, title: str, author: str):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initialize an EBook, calling the base class constructor
        and adding file_size.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation for EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initialize a PrintBook, calling the base class constructor
        and adding page_count.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation for PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize the library with an empty book list."""
        self.books = []

    def add_book(self, book: Book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)
