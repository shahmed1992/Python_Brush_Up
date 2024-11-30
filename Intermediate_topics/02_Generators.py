"""
Generator Theory:
    1. A Generator in Python is a function that returns an iterator using the Yield keyword.
    2. A generator function in Python is defined like a normal function, but whenever it needs to generate a value,
        it does so with the yield keyword rather than return.
    3.Generators differ from standard functions in that they allow you to iterate through a sequence of values over time,
        instead of computing and returning a single result.
    4. Standard Functions: Compute a value and return it once. They use the return statement.
    5. The yield statement is used in a generator function to return a value and pause the function’s execution, preserving its state.
        When next() is called on the generator, execution resumes right after the yield.
    6. Benefits:
        Memory Efficiency: Generators generate values on the fly, reducing memory usage compared to storing the entire sequence in memory.
        Lazy Evaluation: Values are computed only when needed, which can lead to performance improvements, especially with large datasets.
        Maintain State: Generators automatically maintain their state between yield statements, making them suitable for iterative processes.
        Convenience: Generators simplify code for iterating over large datasets or streams of data without needing to manage state explicitly.

Reference: https://www.geeksforgeeks.org/generators-in-python/
"""

# Example-1
# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)
"""
    Output:
        1
        2
        3
"""

# Another way to call the above generator function
x = simpleGeneratorFun()
print(next(x))
print(next(x))
print(next(x))
"""
    Output:
        1
        2
        3
"""

# Example-2
# In this example, we will create two generators for Fibonacci Numbers,
# first a simple generator and second generator using a for loop.
def fib(limit):
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b

# Create a generator object
x = fib(200)

# Iterate over the generator object and print each value
for i in x:
    print(i)