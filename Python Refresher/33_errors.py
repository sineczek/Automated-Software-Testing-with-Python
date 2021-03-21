def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    # TypeError ValueError RuntimeError inne errory
    return dividend / divisor


grades = []

print("Welcome to the average grade program.")
if len(grades) == 0:
    print("You dont have any grades yet!")

try:
    average = divide(sum(grades), len(grades))
    #print(f"Average grade is {average}") #ew. dajemy else:

except ZeroDivisionError as e:
    # print(e)
    print("There are no grades yet in your list!")
else:
    print(f"Average grade is {average}")

finally:
    print("Thank You!")

print("-+"*50)

students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": [50]},
    {"name": "Jen", "grades": [100, 90]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} average {average}")
except ZeroDivisionError as e:
    print(f"Error: {name} has no grades!")
else:
    print("-- All student averages calculated. --")
finally:
    print("-- End of student average calculation. --")



