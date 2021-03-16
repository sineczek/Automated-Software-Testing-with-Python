class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): #magic method - mienia w stringa
        return f"Person {self.name}, {self.age} years old."

    def __repr__(self): # jednoznczny obiekt
        return f"<Person ({self.name}, {self.age})>"

# Person() #tu "woła" __init__

bob = Person("BoB", 35)
# print(bob) # pokaże ciąg rerezentujący bob'a bez __str
print(bob) #__str__ method
