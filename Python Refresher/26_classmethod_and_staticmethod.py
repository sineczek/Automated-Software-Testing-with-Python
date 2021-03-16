class ClassTest:
    def instance_method(self): #do wykorzystywania wewnątrz obiektu, lub do modyfikowania etc.
        print(f"Called instance_method of {self}")

    @classmethod # używane jako "fabryki" ?
    def class_method(cls):
        print(f"Call class_method of {cls}")

    @staticmethod #do tworzenia metod w klasie, rzadko używane
    def static_method():
        print(f"Call static_method")

"""# 2 metody wyzwania dla instance_method
test = ClassTest()
test.instance_method()
# lub
ClassTest.instance_method(test)"""

ClassTest.class_method() #tyle wystarczy dla class_methody
ClassTest.static_method()


# przykład fabryki - classmethod

class Book:
    TYPES = ("hardcover", "paperback") #zmienna staje się właściwością klasy

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        #return Book(name, Book.TYPES[0], page_weight +100) można tak, ale lepiej
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        #return Book(name, Book.TYPES[1], page_weight)
        return cls(name, cls.TYPES[1], page_weight) # - lepiej


print(Book.TYPES)
# book = Book("Harry Poter", "hardcover", 1500) jak dodaliśmy @classmethod to już można jak poniżej
# metodą klasy
book = Book.hardcover("Harry Poter", 1500)
book2 = Book.paperback("Python 101", 600)
print(book)
print(book2)

