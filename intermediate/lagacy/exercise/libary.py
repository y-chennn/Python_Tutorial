class Book:
    def __init__(self, title, author, call_num) -> None:
        self._title = title
        self._author = author
        self._call_num = call_num

    @property
    def num(self):
        return self._call_num

    def __str__(self):
        return f"Book: {self._title} by {self._author} (call number: {self._call_num})"


class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book_by_call_num(self, call_num):
        for book in self.books:
            if book.num == call_num:
                return book
        return None

    def display_books(self):
        if not self.books:
            print("The library is empty")
        else:
            print("Library Books: ")
            for book in self.books:
                print(book)


book1 = Book(title="The Divine Comedy", author="Dante Alighieri", call_num=1)

book2 = Book(title="Les Misérables", author="Victor Marie Hugo", call_num=2)

book3 = Book(title="Le Petit Prince", author="Antoine de Saint-Exupéry", call_num=3)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()
