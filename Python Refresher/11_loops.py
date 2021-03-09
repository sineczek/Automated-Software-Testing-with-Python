'''number = 7
while True:
    user_input = input('EWould You like to play? (Y/n)')



    if user_input == "n":
        break

    user_number = int(input('Guess our number: '))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You ware off by one")
    else:
        print("Sorry! It's wrong!")'''

friends = ["Rolf","Jen","Bob","Anne"]

for f in friends:
    print(f"{f} is my friend")

grades = [35, 57, 98, 100, 100]
total = 0
amount =len(grades)

for g in grades:
    total += g

print(total / amount)




