###################### map functions ######################
# The map() function in Python is a built-in function used for applying a given function 
# to each item in an iterable (e.g., list, tuple). 

# It's used for several reasons:
# 1. Efficiency: Often faster than equivalent for loops.
# 2. Readability: Provides a concise way to transform data.
# 3. Functional programming: Supports a more functional style of coding.
# 4. Lazy evaluation: Returns an iterator, saving memory for large datasets.

# Syntax:
# map(function, iterable, ...)

# Key points:
# 1. Applies the function to every item in the iterable.
# 2. Can take multiple iterables if the function accepts multiple arguments.
# 3. Returns a map object (iterator) which can be converted to a list or used in a loop.

# Use cases:
# - Applying a transformation to all elements in a list
# - Parsing or converting data types in bulk
# - Performing calculations on multiple lists simultaneously

# map() is particularly useful when you need to apply a simple operation to every element 
# in a sequence without modifying the original data. It's a key tool in writing more concise 
# and functional-style Python code.

## example 1 ##
nums = [1, 2, 3, 4, 5]
nums_str = ["1", "2", "3", "4", "5"]
names = ["john", "jane", "doe", "smith"]
users = [
    {"name": "john", "age": 20},
    {"name": "jane", "age": 21},
    {"name": "doe", "age": 22},
    {"name": "smith", "age": 23},
]
square_nums = []

for num in nums:
    square_nums.append(num ** 2)

print(f"example 1-1 square_nums with for loop: {square_nums}")

def square_num(num):
    return num ** 2

square_nums = list(map(square_num, nums))
print(f"example 1-2 square_nums map with function: {square_nums}")

square_nums = list(map(lambda x: x ** 2, nums))
print(f"example 1-3 square_nums map with lambda: {square_nums}")

nums = list(map(int, nums_str))
print(f"example 1-4 nums_str: {nums_str}")
print(f"example 1-4 nums_str map with int function: {nums}")

names = list(map(str.capitalize, names))
print(f"example 1-5 names map with str.capitalize: {names}")

users_name = list(map(lambda user: user["name"].upper(), users))
print(f"example 1-6 users name map with lambda: {users_name}")

users_age = list(map(lambda user: user["age"], users))
print(f"example 1-7 users age map with lambda: {users_age}")