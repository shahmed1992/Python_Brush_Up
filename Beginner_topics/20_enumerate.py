l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

"""
    Output:
        Return type: <class 'enumerate'>
        [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
        [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]
"""

l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)

# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print (count, ele)
"""
Output:
    100 eat
    101 sleep
    102 repeat
"""