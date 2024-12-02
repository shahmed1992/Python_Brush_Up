"""
Lambda expressions or anonymous functions.

Reference: https://www.youtube.com/watch?v=25ovCm9jKfA
"""
# Example-1
# Write function to compute 3x+1
# std approach
def compute_3x_1(x):
    return 3*x+1

res = compute_3x_1(4)
print(res) # Output: 13

# using lambda expression approach
res = lambda x: 3*x+1
print(res(4)) # Output: 13

# Lambda expression with multiple inputs

res1 = lambda x,y: x+y
# res1(145, 890)
print(res1(145,890))