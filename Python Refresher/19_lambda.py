'''def add(x, y):
    return x + y

print(add(5,7))'''

# to samo
add = lambda x, y: x + y  # jeśli jej nie nazwiemy to trzeba
print(add(5, 7))
print((lambda x, y: x + y)(5, 7))  # tego raczej sie nie używa


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence] #to częściej w pythonie niż map, to jest szybsze

#map funkcja
doubled = list(map(double, sequence)) #map przechodzi po sequence w tym wypadku i stosuje double, list aby nie był to map-object


doubled = [(lambda x: x*2)(x)for x in sequence] #to samo z lambdą, raczej nie stosowane, bo ciężkie w odczycie