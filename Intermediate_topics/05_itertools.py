"""
Itertools in python

iterator:

reference: https://www.youtube.com/watch?v=p8FUoSIyIVY&t=502s

"""


# Python program to demonstrate
# infinite iterators

import itertools

# for in loop
for i in itertools.count(5, 5):
	if i == 35:
		break
	else:
		print(i, end=" ")
"""
	Output:
		5 10 15 20 25 30
"""

# Infinite Repeater
for i in itertools.repeat("hello", 5):
	print(i)
"""
	Output:
		hello
		hello
		hello
		hello
		hello
"""


# Infinite Cycle
cycler = itertools.cycle("ABCDEF")
i=0
for j in cycler:
	while i <100:
		print(next(cycler), end=" ")
		i+=1
	break

# Terminating Iterators

list2 = [1,2,3,4,5,6,7,8,9]
list3 = itertools.accumulate(list2)
print()
print(list(list3))
"""
	Output:
		[1, 3, 6, 10, 15, 21, 28, 36, 45]
"""

pair_list = [x for x in range(1, 11)]
paired = itertools.pairwise(pair_list)
print(list(paired))
"""
	Output:
		[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
"""

# Combinatoric Iterators

def product_example(iterable1, iterable2):
	result = itertools.product(iterable1, iterable2)
	print(list(result))
product_example([1,2,3], ["a", "b", "c"])
"""
	Output:
		[(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]
"""

# Permutations

def permutations_example(iterable, size):
	result = itertools.permutations(iterable, size)
	print(list(result))
permutations_example("ABCD", 2)
permutations_example("ABCD", 3)
"""
	Output:
		[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
"""
def combination_example(iterable, size):
	result = itertools.combinations(iterable, size)
	print(list(result))
combination_example("ABCD", 2)
"""
	Output:
		[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
"""

