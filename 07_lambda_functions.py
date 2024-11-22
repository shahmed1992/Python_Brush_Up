# Example-1
s = 'GeeksforGeeks'

upper = lambda string: string.upper()
print(upper(s))

# Example-2


lambda_cube = lambda y: y*y*y
print("Using lambda function, cube:", lambda_cube(5))

# Example-3

is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())

# Resource: https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/