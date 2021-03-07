l = ['Bob', 'Rolf', 'Anne']
t = ('Bob', 'Rolf', 'Anne')  # nie można zmienić zmiennych w tupli!
t1 = ('a',) #tupla z jedną wartością
t2 = 'a', #też tupla
s = {'Bob', 'Rolf', 'Anne'}  # można mieć powtórzone wartości

print(l)

print(l[0])
print(t)
print(t[2])  # przy setach się tak nie da
print(s)

# podmienianie w liście
l[0] = 'Joe'
print(l)

# dodawanie i usówanie
l.append('Bob')
print(l)

l.remove('Anne')
print(l)

print(s)
s.add('Joe')
print(s)