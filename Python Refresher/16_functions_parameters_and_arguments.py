def add(x, y):
    result = x + y
    print(result)


add(5, 3)


def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Michał")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("NO!")


divide(15, 0)
divide(divisor=3, dividend=15)
