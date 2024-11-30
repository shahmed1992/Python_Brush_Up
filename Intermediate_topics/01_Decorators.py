"""
Decorators Theory:
    1. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
    without permanently modifying it.
    2. Before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.
    3. First Class Objects:
        Properties of first class functions:
            A function is an instance of the Object type.
            You can store the function in a variable.
            You can pass the function as a parameter to another function.
            You can return the function from a function.
            You can store them in data structures such as hash tables, lists, …
Reference: https://www.geeksforgeeks.org/decorators-in-python/
"""
# Example 1: Passing the function as an argument
# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)

greet(shout)
greet(whisper)
"""
    Output:
        HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
        hi, i am created by a function passed as an argument.
"""

# Example 2: Returning functions from another function.

# Python program to illustrate functions
# Functions can return another function
def create_adder(x):
    print(f"{x=}")
    def adder(y):
        print(f"{y=}")
        return x+y

    return adder

add_15 = create_adder(15)

print(add_15(10))
"""
    Output:
        x=15
        y=10
        25
"""

# Decorator
# importing libraries
import time
import math


# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    print("At 1")
    def inner1(*args, **kwargs):
        # storing time before function execution
        print("At 2")
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
        print("At 5")
    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 3 seconds because it takes very less time
    # so that you can see the actual difference
    print("At 3")
    print(f"Calculating Factorial of {num}")
    time.sleep(3)
    print(math.factorial(num))
    print("At 4")

# calling the function.
factorial(10)
"""
    Output:
        At 1
        At 2
        At 3
        Calculating Factorial of 10
        3628800
        At 4
        Total time taken in :  factorial 3.000251054763794
        At 5    
"""