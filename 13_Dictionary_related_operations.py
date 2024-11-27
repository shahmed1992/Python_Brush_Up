"""
    1. Create dictionary comprehension with key as number and cube of the number as value
    2. Iterating over dictionary using items, keys
    3. Nested dictionary
    4. updating inner elements in the dictionary
    5. create a dict having key as the word of a string and value as the number of occurences of the word in the string.

"""

# Example - 1
# 1. Create dictionary comprehension with key as number and cube of the number as value
dict_cube = {x:x**3 for x in range(1, 20) if x%2==1}
print(dict_cube)
"""
Output:
    {1: 1, 3: 27, 5: 125, 7: 343, 9: 729, 11: 1331, 13: 2197, 15: 3375, 17: 4913, 19: 6859}
"""

# Example-2
# 2. Iterating over dictionary using items, keys
for key, value in dict_cube.items():
    # print(f"{key=}, {value=}")
    pass
# Example-3 and Example-4
# 3. Nested dictionary
#  Adding AllowableValues to AMT Loop Count,
# Consider maxvalue and min value as the elements of that list.
Attributes= {
    "AMT Loop Count": {
      "DataType": "number",
      "MaximumValue": 65535,
      "MinimumValue": 0,
      "default_value": "1",
    },
    "CPU CrashLog": {
      "AllowableValues": [
        "Disabled",
        "Enabled",
        "Auto"
      ],
      "DataType": "string",
      "default_value": "Auto",
    },
	}
max_value = Attributes["AMT Loop Count"]["MaximumValue"]
min_value = Attributes["AMT Loop Count"]["MinimumValue"]
Attributes["AMT Loop Count"]["AllowableValues"] = [max_value, min_value]
print(Attributes)

# Example-5
# create a dict having key as the word of a string and value as the number of occurences of the word in the string.
from collections import Counter
input_str1 = """A garden enhances the beauty of our home. 
In the open space on the left side of the entrance of our house, 
green pleasing groves are loved by all. There are various colours in this flower, 
vines are red and pink when these flowers bloom in the first rays of the sun, 
they are made to see the sight of the garden, and butterflies hover over them.  Many birds make their 
nests on trees and the sound of their chirping in the morning and evening sounds very adorable."""
str_words = Counter(input_str1.split(" "))
print(str_words)
# print(input_str1)
