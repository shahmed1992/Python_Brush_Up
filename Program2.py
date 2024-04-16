

"""

Description: 

        Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 
Sample input & output

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
"""
def swapNumbers(list1, pos1, pos2):
    try:
        if pos1<0 or pos1>(len(list1)-1) or pos2<0 or pos2>(len(list1)-1):
            raise Exception(f"Positions must be between 0 and {len(list1)-1}")
        else:
            list1[pos1],list1[pos2] = list1[pos2],list1[pos1]
        return list1
    except :
        print("#"*50)
        print("Exception Caught")
        print(f"Positions must be between 0 and {len(list1)-1} for the input provided.")
        print("#"*50)
input_list = [23, 65, 19, 90]
pos1 = 1
pos2 = 4
print("Before:")
print(input_list)
print("After:")
print(swapNumbers(input_list,pos1,pos2))

