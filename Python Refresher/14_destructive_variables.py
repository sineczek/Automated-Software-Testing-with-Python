x = 5, 10  # tupla
x, y = 5, 10

tupla = 5, 11
x, y = tupla
print(x, y)

print("-"*30)

students_attendance = {"Rolf": 96, "Adam": 80, "Anne": 100}

print(list(students_attendance.items())) #list tupli

for s, attendance in students_attendance.items():
    print(f"{s}: {attendance}")

print("-"*30)

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, proffesion in people:
    print(f"Name: {name}, Age: {age}, Proffesion: {proffesion}")

print("-"*30)
person = ("Bob", 42, "Mechanic")
#jak zmienna opisana jest _ to ma być ignorowana (taki standard)

name, _, proffesion = person

print(name, proffesion)

print("-"*30)

head, *tail = [1,2,3,4,5]
#*tail wszystkie inne wartości
#*head zbierze wszystkie prócz ostatniej

print(head)
print(tail)
print("-"*30)





