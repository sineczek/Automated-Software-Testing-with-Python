# mutable czyli zmienne ;]
# immutable czyli niezmienne są: tuple, łańcuchy, liczby całkowice, zmienno przecinkowe i wartości logiczne (boolean)


a = []
b = a

print(id(a))
print(id(b))

a.append(35)

print(id(a))
print(id(b))

b = []

print(id(a))
print(id(b))

a = 8578
b = 8578

print(id(a))
print(id(b))

a = 8579

print(id(a))
print(id(b))

a = "hello"
b = a
print(id(a))
print(id(b))

a += "world"

print(id(a))
print(id(b))
