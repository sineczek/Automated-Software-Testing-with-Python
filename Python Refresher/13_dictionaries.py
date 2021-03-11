friends_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

friends_ages["Bob"] = 20 #dodawanie/zmiana istniejącego

print(friends_ages["Adam"])

#lista słowników
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
]
print(friends)
print(friends[1])
print(friends[1]["name"])
print("-"*100)

students_attendance = {"Rolf": 96, "Adam": 80, "Anne": 100}

for s, attendance in students_attendance.items():
    print(f"{s}: {attendance}")
'''nie najlepsza opcja
for s in students_attendance:
    #print(s)
    print(f"{s}: {students_attendance[s]}%")'''

#tylko klucze tak można
if "Bob" in students_attendance:
    print(f"Bob: {students_attendance['Bob']}")
else:
    print("Bob is not a student in this class")

attendance_values = students_attendance.values()
print(sum(attendance_values) / len(attendance_values))


