###################### filter function ######################
# The filter() function in Python is a built-in function used to filter elements from an iterable based 
# on a given function. 

# It's used for several reasons:
# 1. Efficiency: Often more concise and faster than equivalent for loops.
# 2. Readability: Provides a clear, functional way to filter data.
# 3. Lazy evaluation: Returns an iterator, saving memory for large datasets.
# 4. Functional programming: Supports a more functional style of coding.

# Syntax:
# filter(function, iterable)

# Key points:
# 1. The function should return True for items to keep, False for items to filter out.
# 2. Returns a filter object (iterator) which can be converted to a list or used in a loop.
# 3. If the function is None, it filters out falsy values (0, False, None, empty containers).

# Use cases:
# - Removing unwanted elements from a sequence
# - Selecting data that meets certain criteria
# - Cleaning datasets by removing invalid entries
# - Implementing search functionality

# filter() is particularly useful when you need to selectively keep elements from a sequence 
# based on a condition. It allows for clean, expressive code when working with data filtering tasks, 
# and is a key component in writing more functional-style Python code.

## example 1
numbers = [1,2,5,-2,7,-3,8]

def is_negative(num):
    if num < 0:
        return True
    else:
        return False

negative_numbers = list(filter(is_negative, numbers))
print(f"Example 1-1 negative_numbers with function: {negative_numbers}")

negative_numbers = list(filter(lambda x: x < 0, numbers))
print(f"Example 1-2 negative_numbers with lambda: {negative_numbers}")

odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
print(f"Example 1-3 odd_numbers with lambda: {odd_numbers}")

## example 2

names = ["ali","ahmet","canan","ayse","fatma","can", "cem"]

filtered_result = list(filter(lambda x: len(x) > 4, names))
print(f"Example 2-1 result with filter: {filtered_result}")

filtered_result = list(map(lambda x: x.upper(), filtered_result))
print(f"Example 2-2 filtered_result with map: {filtered_result}")


## example 3

users = [
    {"username": "ali", "age": 20, "posts": ["post1","post2"]},
    {"username": "ahmet", "age": 25, "posts": ["post3","post4","post5","post6"]},
    {"username": "canan", "age": 30, "posts": []},
    {"username": "ayse", "age": 35, "posts": ["post13","post14","post15"]},
    {"username": "fatma", "age": 40, "posts": ["post7","post8"]},
    {"username": "can", "age": 45, "posts": ["post9","post10"]},
    {"username": "cem", "age": 50, "posts": ["post11","post12"]},
]

filtered_users = list(filter(lambda u: u["age"] > 30, users))
print(f"Example 3-1 filtered_users with filter: {filtered_users}")

post_result = list(filter(lambda u: len(u["posts"])>2, users))
print(f"Example 3-2 post_result with filter: {post_result}")

# filtered_names = list(map(lambda u: u["username"].upper() , post_result))
filtered_names = list(map(lambda u: u["username"].upper() , filter(lambda u: len(u["posts"])>2, users)))
print(f"Example 3-3 filtered_names with map: {filtered_names}")

filtered_names = [u["username"].upper() for u in users if len(u["posts"])>2]
print(f"Example 3-4 filtered_names with list comprehension: {filtered_names}")




