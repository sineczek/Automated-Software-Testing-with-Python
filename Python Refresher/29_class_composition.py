"""
Kompozycje są jak dziedziczenie, ale są dużo cześciej używane z uwagi na to,
że mniej kodu i łatwiejszy kod jest potrzebny

"""

class BookShelf:
    def __init__(self, *books): # kompozycja na półce jest wiele książek
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."



"""
dziedziczenie trochę bez sensu, bo na półce mogą być książki, ale książki nie są półką
i tu wchodzi w grę kompozycja
"""

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)
print(shelf)