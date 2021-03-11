numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]  # lepsze

# klasyczne
# for num in numbers:
#    doubled.append(num*2)


firnds = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [f for f in firnds if f.startswith("S")]
print(starts_s)
'''klasycznie
for f in friends:
    if f.startswith("S")
        starts_s.append(f)'''

