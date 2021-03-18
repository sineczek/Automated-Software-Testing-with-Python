from typing import List  # Tuple, set etc.


def list_avg(sequence: List) -> float:  # przyjmuje liste -> a zwraca float
    return sum(sequence) / len(sequence)


list_avg(123)


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):  # hinting, czyli podpowie, że name ma być stringiem ...
        self.name = name
        self.weight = weight
        self.book_type = book_type

    def __repr__(self) -> str:
        return f"BookShelf {self.name}, {self.book_type}, weight {self.weight} g."

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":  # zwracają obiekt taki jak klasa, muszą być ""
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)


class BookShelf:
    def __init__(self, book: List[Book]):  # hint: book to lista książek - inna klasa
        self.books = book

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."
