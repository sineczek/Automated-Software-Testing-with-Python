student = {"name":"Rolf", "grades":(89,90,93,78,90)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student["grades"]))


class Student:
    def __init__(self, name, grades): #metoda
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)



student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Rolf", (90, 90, 93, 78, 90))# tworzy obiekt
print(student.name)
print(student.grades)
print(average(student.grades)) #to do funkcji
print(Student.average(student)) #metoda z klasy
print(student.average()) #lepsze odwołanie do metody klassy
print(student2.name)
print(student2.grades)
print(student2.average())