# valid variable name
geeks = 1
Geeks = 2
Ge_e_ks = 5
_geeks = 6
geeks_ = 7
_GEEKS_ = 8

print(geeks, Geeks, Ge_e_ks)
print(_geeks, geeks_, _GEEKS_)

# Variables Assignment in Python
# Here, we will define a variable in python. Here, clearly we have assigned a number,
# a floating point number, and a string to a variable such as age, salary, and name.

# An integer assignment
age = 45

# A floating point
salary = 1456.8

# A string
name = "John"

print(age)
print(salary)
print(name)
"""
    Output:
        45
        1456.8
        John
"""
a, b, c = 1, 20.2, "GeeksforGeeks"

print(a)
print(b)
print(c)
"""
    Output:
      GeeksforGeeks
  
"""

# How does + operator work with variables?
# The Python plus operator + provides a convenient way to add a value if it is a number and concatenate if it is a string.
# If a variable is already created it assigns the new value back to the same variable

a = 10
b = 20
print(a+b)

a = "Geeksfor"
b = "Geeks"
print(a+b)

"""
Output:
    30
    GeeksforGeeks
"""

# numberic
var = 123
print("Numeric data : ", var)

# Sequence Type
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

# Boolean
print(type(True))
print(type(False))

# Creating a Set with
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

"""
    Output:
        Numeric data :  123
        String with the use of Single Quotes: 
        Welcome to the Geeks World
        <class 'bool'>
        <class 'bool'>
        Set with the use of String: 
        {'r', 'G', 'e', 'k', 'o', 's', 'F'}
        Dictionary with the use of Integer Keys: 
        {1: 'Geeks', 2: 'For', 3: 'Geeks'}

"""