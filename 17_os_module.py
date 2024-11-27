"""
OS Module in python
    1. Important methods of OS -
    2. Handling the Current Working Directory
    3. Creating a Directory
    4. Listing out Files and Directories with Python
    5. Deleting Directory or Files using Python


"""
import os

# 1. Important methods of OS Module

# 2. Handling the Current Working Directory
curr_dir = os.getcwd()
print(curr_dir)

# 3. Creating a Directory
new_dir = "new_dir"
try:
    os.mkdir(f"{os.getcwd()}/{new_dir}")
except FileExistsError:
    print("Dir Already exists")

# 4. Listing out Files and Directories with Python
list_dir = os.listdir(os.getcwd())
print(list_dir)

# 5. Deleting Directory or Files using Python
# OS module provides different methods for removing directories and files in Python. These are –
#
# Using os.remove()
# Using os.rmdir()

os.rmdir(f"{os.getcwd()}/{new_dir}")
