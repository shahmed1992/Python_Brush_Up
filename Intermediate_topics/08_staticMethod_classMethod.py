"""
    1. Class Method in python
        a. The @classmethod decorator used
        b. A class method receives the class as an implicit first argument, just like an instance method receives the instance
          class C(object):
                @classmethod
                def fun(cls, arg1, arg2, ...):
                   ....
          fun: function that needs to be converted into a class method
          returns: a class method for function.
        c. A class method is a method that is bound to the class and not the object of the class.
    2. Static Method in python
        a. A static method does not receive an implicit first argument.
        b. A static method is also a method that is bound to the class and not the object of the class.
        c. This method can’t access or modify the class state.
        d. It is present in a class because it makes sense for the method to be present in class.

        Syntax Python Static Method:

        class C(object):
            @staticmethod
            def fun(arg1, arg2, ...):
                ...
        returns: a static method for function fun.

"""
# Example-1
# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))