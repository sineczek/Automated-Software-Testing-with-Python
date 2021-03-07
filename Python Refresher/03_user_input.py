name = input('Enter Your name: ')
print(name)

size_input = input('How big is Your house (in m): ')
square_meters = int(size_input)
square_feet = square_meters * 10.8
print(size_input+'m2')
print(f'{square_meters} square meters is {square_feet:.2f} square feet') #:.2f postara się sformatować do 2 miejsc

