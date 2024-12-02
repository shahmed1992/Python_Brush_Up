# Reference: https://www.geeksforgeeks.org/python-classes-and-objects/
# Example-1
#  instantiating a class
class Dog:

    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()

# Example-2

class ClassExample:

    def __init__(self, name, company):
        self.name = name
        self.company = company

    def show(self):
        print("Hello my name is " + self.name +
              " and I work in "+self.company+".")

    def __str__(self):
        return f"My name is {self.name} and I work in {self.company}."
obj = ClassExample("Hussain", "LTI")
obj.show()
print(obj) # prints using str method

# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

# Class for Dog


class Dog:

    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color):

        # Instance Variable
        self.breed = breed
        self.color = color


# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)
"""
    Output:
        Rodger details:
        Rodger is a dog
        Breed:  Pug
        Color:  brown
        
        Buzo details:
        Buzo is a dog
        Breed:  Bulldog
        Color:  black
        
        Accessing class variable using class name
        dog

"""