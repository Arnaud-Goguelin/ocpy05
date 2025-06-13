from datetime import datetime


class Book:
    """Represents a book with a title, an author, and a publication year.
    Provides functionality for validating the title, author, and year attributes.

    Attributes:
        title (str): The title of the book. Must be a non-empty string.
        author (str): The author of the book. Must be a non-empty string.
        year (int): The publication year of the book. Must be a non-negative integer.
    """

    def __init__(self, title: str, author: str, year: int):
        self.title: str = self.validate_title_and_author(title)
        self.author: str = self.validate_title_and_author(author)
        self.year: int = self.__validate_year(year)

    def __setattr__(self, name: str, value: str | int) -> None:
        """Intercepts attribute assignment for validation."""
        if name in ("title", "author"):
            value = self.validate_title_and_author(value)
        if name == "year":
            value = self.__validate_year(value)
        super().__setattr__(name, value)

    @staticmethod
    def validate_title_and_author(value: str) -> str:
        """Validates that a given account holder is a non-empty string."""
        if not isinstance(value, str):
            raise TypeError("A title or an author must be a string")
        if value.isdigit():
            raise ValueError("A title or an author holder cannot be a number")
        if not value.strip():
            raise ValueError("A title or an author holder cannot be empty")
        return value

    @staticmethod
    def __validate_year(value: int) -> int:
        """Validates that a given year is a non-negative integer."""
        if not isinstance(value, int):
            raise ValueError("A year must be an datetime object")
        if value < 0:
            raise ValueError("A year cannot be negative")
        if value > datetime.now().year:
            raise ValueError("A year cannot be in the future")
        return value


class Library:
    """
    Represents a library system for managing book collections and borrowing.

    This class allows for adding books to the library, removing books,
    borrowing and returning books, and viewing available and borrowed books.

    Attributes:
        books (set[Book]): Collection of books available in the library.
        borrowed_books (set[Book]): Collection of books currently borrowed from the library.
    """

    def __init__(self):
        self.books: set[Book] = set()
        self.borrowed_books: set[Book] = set()

    def add_book(self, book: Book) -> None:
        """
        Adds a book to the library collection.

        Args:
            self: Represents the instance of the class.
            book: Book object to be added to the library collection.

        Raises:
            ValueError: If the provided book object is empty.
        """
        if not book:
            raise ValueError("Book cannot be empty to be added to Library")
        if not isinstance(book, Book):
            raise ValueError("Book must be a Book object to be added to Library")
        self.books.add(book)

    @staticmethod
    def __validate_book_title(book_title: str) -> str:
        """Validates that a given book title is a non-empty string."""
        return Book.validate_title_and_author(book_title)

    @staticmethod
    def __found_book_by_title(book_title: str, collection: set[Book]) -> Book | None:
        """
        Retrieves a `Book` object from the collection based on its title.

        Args:
            book_title: The title of the book to search for.

        Returns:
            Book: The first book from the collection that matches the provided title.
        """
        return next((book for book in collection if book.title == book_title), None)

    def remove_book(self, book_title: str) -> None:
        """
        Removes a book from the library's collection based on the provided title.

        Args:
            book_title: The title of the book to be removed from the library.

        Raises:
            ValueError: If the book is not found in the library's collection.

        """
        valide_book_title = self.__validate_book_title(book_title)
        book_to_remove = self.__found_book_by_title(valide_book_title, self.books)
        if not book_to_remove:
            raise ValueError("Book not found in Library")
        self.books.remove(book_to_remove)

    def borrow_book(self, book_title: str) -> None:
        """
        Allows a user to borrow (remove from self.books, add to self.borrowed_books)
        a book from the library if it is available for borrowing.

        Args:
            book_title: The title of the book the user wants to borrow.

        Raises:
            ValueError: If the book is not found in the library's collection.
            ValueError: If the book has already been borrowed.
        """
        valide_book_title = self.__validate_book_title(book_title)
        book_to_borrow = self.__found_book_by_title(valide_book_title, self.books)
        if not book_to_borrow:
            raise ValueError("Book not found in Library")
        if book_to_borrow in self.borrowed_books:
            raise ValueError("Book already borrowed")
        self.books.remove(book_to_borrow)
        self.borrowed_books.add(book_to_borrow)

    def return_book(self, book_title: str) -> None:
        """
        This method allows a user to return a borrowed book back
        (remove from self.borrowed_books, add to self.books) to the library.

        Args:
            book_title: The title of the book to be returned.

        Raises:
            ValueError: If the book is not found in the borrowed books list.
            ValueError: If the book is already in the library's available books.
        """
        valide_book_title = self.__validate_book_title(book_title)
        book_to_return = self.__found_book_by_title(valide_book_title, self.borrowed_books)
        if not book_to_return:
            raise ValueError("Book not found in borrowed books list")
        if book_to_return not in self.borrowed_books:
            raise ValueError("Book is already in Library")
        self.books.add(book_to_return)
        self.borrowed_books.remove(book_to_return)

    @property
    def available_books_list(self):
        """Returns a list of titles of books that are available for borrowing."""
        return [book.title for book in self.books]

    @property
    def borrowed_books_list(self):
        """Returns a list of titles of books that are currently borrowed by users."""
        return [book.title for book in self.borrowed_books]


if __name__ == "__main__":
    try:
        first_book = Book("The First Book", "Random Author", 2000)
        second_book = Book("The Second Book", "Another Random Author", 2001)
        test_library = Library()
        test_library.add_book(first_book)
        test_library.add_book(second_book)
        print(test_library.available_books_list)
        print(test_library.borrowed_books_list)
        test_library.borrow_book("The Second Book")
        print(test_library.available_books_list)
        print(test_library.borrowed_books_list)
        test_library.return_book("The Second Book")
        print(test_library.available_books_list)
        print(test_library.borrowed_books_list)
        test_library.remove_book("The Second Book")
        print(test_library.available_books_list)
        print(test_library.borrowed_books_list)
        test_library.borrow_book("The Second Book")

    except (ValueError, TypeError) as error:
        print("An error happened:")
        print(error)
