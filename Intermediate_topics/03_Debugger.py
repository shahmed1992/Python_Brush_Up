"""
    Debugger Theory:
        1. Debugging in Python is facilitated by pdb module (python debugger) which comes built-in to the Python standard library.
        2. It is actually defined as the class Pdb which internally makes use of bdb(basic debugger functions)
        3. pdb runs purely in the CLI, making it great for debugging code on remote servers when we don’t have the privilege of a GUI-based debugger.
        4. Few commands to type in debugging mode
            help	To display all commands
            where	Display the stack trace and line number of the current line
            next	Execute the current line and move to the next line ignoring function calls
            step	Step into functions called at the current line
            whatis  to check the type of a variable
    Reference: https://www.geeksforgeeks.org/python-debugger-python-pdb/
"""
# Example-1
import pdb
def addition(a, b):
	answer = a * b
	return answer

pdb.set_trace()
x = input("Enter first number : ")
y = input("Enter second number : ")
sum = addition(x, y)
print(sum)
