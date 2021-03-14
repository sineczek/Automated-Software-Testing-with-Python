users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "long4password"),
    (3, "username", "1234")
]

#dictionary comprehension
username_mapping = {user[1]:user for user in users} #kluczami jest username, a wartościami są całe tuple
print(username_mapping)

print(username_mapping["Bob"]) #sama tupla

'''#to samo ale w długiej formie - mniej strosowane
for user in users:
    if user[1] == "Bob":
        print(user)'''

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input] # _ fo będzie rónież id

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect!")

