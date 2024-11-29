"""
    1. To look into the functinality of sorted function in python
    2. Syntax of sorted() function
        sorted(iterable, key=None, reverse=False)
    3. Using key and lambda



"""
a = [4, 1, 3, 2]
#Using sorted function to modify list in-place
b = sorted(a)
print(f"{b=}")
print(f"{a=}")

c = sorted(a, reverse=True)
print(f"{c=}")

aa = ["apple", "banana", "cherry", "date"]
res = sorted(aa, key=len)
print(f"{res=}")


# Using
a2 = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 91},
    {"name": "Eve", "score": 78}
]

# Use sorted() to sort the list 'a' based on the 'score' key
# sorted() returns a new list with dictionaries sorted by the 'score'
b2 = sorted(a2, key=lambda x: x['score'], reverse=True)
print(b2)