# For loops

print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

print("\nDictionary Iteration")
d = dict({'x': 123, 'y': 354})
for i in d:
    print("%s  %d" % (i, d[i]))

print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i)

# While loop

fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break

