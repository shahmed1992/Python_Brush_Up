"""
Map function
    1. convert list of nums(which are in str format) to list of ints
    2. map Using lambda function (double each number in the list and create a new list)
    3. convert each element in the list to upper case
    4. Get only first char from each word and store it in a new list
    5. Removing white spaces from strings
"""
# Example-1
#     1. convert list of nums(which are in str format) to list of ints
s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))
"""
    Output:
        [1, 2, 3, 4]
"""
# Example-2
#   2. map Using lambda function (double each number in the list and create a new list)
a = [1, 2, 3, 4]

# Using lambda function in "function" parameter
# to double each number in the list
res = list(map(lambda x: x * 2, a))
print(res)
"""
    Output:
        [2, 4, 6, 8]
"""
# Example-3
# 3. conver each element in the list to upper case
fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))

"""
    Output:
        ['APPLE', 'BANANA', 'CHERRY']
"""

# Exampl-4:
# 4. Get only first char from each word and store it in a new list
words = ["apple", "banana", "cherry"]
first_char_list = list(map(lambda s: s[0], words))
print(first_char_list)
"""
    Output:
        ['a', 'b', 'c']
"""
# Example-5
# Removing white spaces from strings
example_5 = [" hello ", " there  ", "this ", " is ", " example - 5   "]
res_list = list(map(lambda x: x.strip(), example_5))
print(res_list)
"""
    Output:
        ['hello', 'there', 'this', 'is', 'example - 5']
"""

# Example-6
# 6. Convert Fahrenheit from celsius using map and lambda
# formula: (c*9/5)+32
temp_celsius = [0,20,37, 100]
temp_fah = list(map(lambda x: x*(9/5)+32, temp_celsius))
print(temp_fah)
"""
    Output:
        [32.0, 68.0, 98.60000000000001, 212.0]
"""

# Example-
#
"""
    Output:
        
"""

# Reduce

