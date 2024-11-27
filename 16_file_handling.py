"""
File handling examples for quick references.
    1. Using open()
    2. using with() (this is also known as context manager)
    3. Working in Write Mode using open
    4. working in write mode using with
"""

# Example-1
# File handling using open in python
file = open("file_01", "r")
for line in file:
    print(line)
file.close()
"""
    Output:
        Hello world

        GeeksforGeeks

        123 456
"""
# Example-2
# 2. using with() (this is also known as context manager)
with open("file_01", "r") as fopen:
    file_contents = fopen.readlines()
    print(file_contents)
"""
    Output:
        ['Hello world\n', 'GeeksforGeeks\n', '123 456\n']
"""

# Example-3
# Working in Write Mode
# Python code to create a file
file = open("file_03.txt", "w")
file.write("THis is line-1 in file_03\n")
file.write("This is line-2 in file_03")
file.close()
"""
    Output:

"""


# Example-4
# 4. working in write mode using with
with open("file_04.txt", "w") as file4:
    file4.write("This is line-1 in file-4\n")
    file4.write("This is line-2 in file-4\n")
"""
    Output:

"""

# Example-5
# 5. Append mode using with
with open("file5.txt", "a") as file5:
    file5.write("Line-1 in file5\n")
    file5.write("Line-2 in file5")
"""
    Output:

"""