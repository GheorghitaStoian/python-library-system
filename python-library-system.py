class Book:
    def __init__(self, title, autor, year):
        self.title = title
        self.autor = autor
        self.year = year

    def __str__(self):
        return f"{self.title} - {self.autor} ({self.year})"


class FictionBook(Book):
    def __init__(self, title, autor, year, genre):
        super().__init__(title, autor, year)
        self.genre = genre

    def __str__(self):
        return f"{self.title} - {self.autor} ({self.year}), Genre: {self.genre}"


class ScienceBook(Book):
    def __init__(self, title, autor, year, field):
        super().__init__(title, autor, year)
        self.field = field

    def __str__(self):
        return f"{self.title} - {self.autor} ({self.year}), Field: {self.field}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

    def find_by_title(self, title):
        results = []
        for book in self.books:
            if book.title == title:
                results.append(book)
        return results

    def remove_book(self, title):
        new_list = []
        for book in self.books:
            if book.title != title:
                new_list.append(book)
        self.books = new_list

    def find_by_autor(self, autor):
        results = []
        for book in self.books:
            if book.autor == autor:
                results.append(book)
        return results

    def get_fiction(self):
        results = []
        for book in self.books:
            if isinstance(book, FictionBook):
                results.append(book)
        return results

    def get_science(self):
        results = []
        for book in self.books:
            if isinstance(book, ScienceBook):
                results.append(book)
        return results


lib = Library()

book1 = Book("Dune", "Frank Herbert", 1965)
book2 = FictionBook("Dune1", "Frank Herbert", 1965, "Sci-Fi")
book3 = ScienceBook("Dune2", "Frank Herbert", 1965, "Physics")
book4 = ScienceBook("Dune3", "Frank Herbert", 1965, "Science")

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_book(book4)

print("These are the number of books that are currently in the library: ")
print(len(lib))

print("\n")

print("Theese are currently all the books: ")
for book in lib.books:
    print(str(book))

print("\n")

print("Fiction books: ")
fic = lib.get_fiction()
for book in fic:
    print(book)

print("\n")

print("Science books: ")
sci = lib.get_science()
for book in sci:
    print(book)

print("\n")

lib.remove_book("Dune")
print("This is how many books are left: ")
print(len(lib))

print("\n")

print("Theese are all the books that are left: ")
for book in lib.books:
    print(str(book))
