def multiply(*args):  # wiele argumentów zbiera (pakuje) w tuple
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total


print(multiply(1, 3, 5))


def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))  # rozkładanie (rozpakowuje) argumentów

nums = {"x": 15, "y": 25}
print(add(nums["x"], nums["y"]))
print(add(**nums)) #to samo ale ładniej, wartość będzie połączona z kluczem

def apply(*args, operator): #zbierz wszystkie argumenty a na końcu jest nazwany argument
    if operator == "*":
        return multiply(*args) #musi tu być * aby nie przekazało tupli
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

print(apply(1,3,6,7, operator="+"))
print(apply(1,3,6,7, operator="*"))
