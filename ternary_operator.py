
# Ternary operator in python

# Program to demonstrate ternary operator
a = 10
b = 20

# python ternary operator
min = "a is minimum" if a < b else "b is minimum"

print(min)

# Example - 2
# Python program to demonstrate nested ternary operator
a, b = 10, 20

print("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")

# Resource: https://www.geeksforgeeks.org/ternary-operator-in-python/