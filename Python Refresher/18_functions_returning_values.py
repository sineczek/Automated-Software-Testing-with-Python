'''def add(x, y): #funkcje zwracają None
    print(x + y)


add(5, 8)
result = add(5, 8)
print(result) #tu byłoby None'''
def add(x, y):
    return x + y #zwraca wartość ale i kończy funkcję

add(5, 8)
result = add(5, 8)
print(result) #tu byłoby None

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "NO!"


result = divide(15, 3)
print(result)