"""

    1. Converting a string to char array
    2. Converting a string to int array ( in case the elements in the array are integers)
    3. Coverting a list to string
    4. Converting a char array to string.
    5. fstrings
    6. Raw strings in python
"""
#     1. Converting a string to char list
str1 = "Hello world"
char_list = [char for char in str1]
print(char_list)

"""
    Output:
        ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

"""

# 2. Converting a string to int array ( in case the elements in the string are integers)
int_str = "1234567890"
int_list = [int(num) for num in int_str]
print(int_list)
"""
    Output:
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
"""

# 3. Coverting a list to string

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
input_list_str = [str(num) for num in input_list]
output_str = "".join(input_list_str)
print(output_str)

# 4. char list to string
input_list1 = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
output_str1 = "".join(input_list1)
print(output_str1)

# 5. f-strings in python
var1 = "Hussain"
print(f"Hello my name is {var1}")

# 6. r-strings in python: raw strings
# used especially in regexes
# Python program to use raw strings

# Define string with r before quotes
# and assign to variable
s1 = r'Python\nis\easy\to\learn'

print(s1)

"""
Output:
    Python\nis\easy\to\learn
"""


