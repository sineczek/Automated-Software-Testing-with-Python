friends = {'Bob','Rolf','Anne'}
abrod = {'Bob', 'Anne'}

#local_friends = {'Rolf'} #hardcoded

local_friends = friends.difference(abrod) #z setu odejmie drugi
print(local_friends)

local_friends = abrod.difference(friends) #pokaże pusty set()
print(local_friends)

local = {'Rolf'}
abrod = {'Bob', 'Anne'}

friends = local.union(abrod) #łączenie setów
print(friends)

art = {'Bob','Jen','Rolf','Charlie'}
science = {'Bob','Jen','Adam','Anne'}

both = art.intersection(science) #wspólne elementy setów
print(both)







