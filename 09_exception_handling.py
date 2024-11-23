# Resource: https://www.geeksforgeeks.org/python-exception-handling/

# Example-1
def fun(a):
    if a < 4:
        b = a / (a - 3)
    print("Value of b = ", b)


try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

"""
    Output:
        ZeroDivisionError Occurred and Handled
        If you comment on the line fun(3), the output will be 
        
        NameError Occurred and Handled
"""
# try with else block
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
"""
    Output:
        -5.0
        a/b result in 0
"""

# Finally keyword
try:
    k = 5//0
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print('This is always executed')
"""
    Output:
        Can't divide by zero
        This is always executed
"""

# Raising Custom exception:
class CustomException(Exception):
    pass


try:
    raise CustomException("Hi there")
except CustomException:
    print ("An exception")
    raise