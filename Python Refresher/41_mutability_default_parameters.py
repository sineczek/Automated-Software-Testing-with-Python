from typing import List, Optional


class Student:
    # def __init__(self, name: str, grades: List[int] = []):  # to jest złe, bo jest to mutable
    def __init__(self, name: str, grades: Optional[List[int]] = None):  # nie koniecznie lista na początku
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)  # nie było rolf.take_exam a i tak ma wartość bo w definicy było grades: List[int] = []
