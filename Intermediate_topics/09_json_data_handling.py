"""
Handling json data using python

1. json.loads - for converting string to dict
2. json.load  - returns JSON object as a dictionary
3. json.dumps - dict to json
"""

s = '{"id":01, "name": "Emily", "language": ["C++", "Python"]}'
print(type(s))

# Python program to convert JSON to Python
import json

# JSON string
employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'

# Convert string to Python dict
employee_dict = json.loads(employee)

print(employee_dict)

print(employee_dict['name'])



# Opening JSON file
f = open('091_data.json',)

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['emp_details']:
	print(i)

# Closing file
f.close()

# Python program to convert
# Python to JSON

# Data to be written
dictionary = {
"id": "04",
"name": "sunil",
"department": "HR"
}

# Serializing json
json_object = json.dumps(dictionary, indent = 4)
print(json_object)


