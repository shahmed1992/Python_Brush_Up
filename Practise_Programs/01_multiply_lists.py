

"""
there are two lists and you want to multiply their elements.

"""
import operator
list1 = [x for x in range (10, 35) if x%3==0]
list2 = [x for x in range (30, 65) if x%3==0]
print(list1)
print(list2)
list3 = list(map(operator.mul, list1, list2))
print(list3)
