name = 'Bob'
greeting = f'Hello, {name}' #f dodało na stałe zmienną

print(greeting)

name = 'Rolf'

print(greeting)

name = 'Bob'
print(f'Hello, {name}')

name = 'Rolf'
print(f'Hello, {name}')

#temlate

name = 'Bob'
greeting = 'Hello, {}'
with_name = greeting.format(name)

print(with_name)
print(greeting.format(name))

longer_phrase = 'Hello, {}. Today is {}.'
formatterd = longer_phrase.format('Rolf','Monday')
print(formatterd)


