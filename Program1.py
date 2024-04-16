#Python Program to interchange first and last elements in a list
"""
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
"""

# Approach-1
list1 = [12, 35, 9, 56, 24]
print("Before")
print(list1)
list1[-1], list1[0] = list1[0], list1[-1]
print("After")
print(list1)


# Approach-2

if len(list1) >= 2:
        # Swap the first and last elements using slicing
        list1 = list1[-1:] + list1[1:-1] + list1[:1]
