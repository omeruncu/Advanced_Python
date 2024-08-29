###################### any and all ######################
# any() and all() are built-in functions in Python used for sequence evaluation. 
# They're particularly useful for checking conditions across iterable objects.

#any():
#1. Purpose: Returns True if any element in the iterable is True.
#2. Usage: Checks if at least one item meets a condition.
#3. Syntax: any(iterable)

#all():
#1. Purpose: Returns True if all elements in the iterable are True.
#2. Usage: Checks if all items meet a condition.
#3. Syntax: all(iterable)

# Why use them:
# 1. Conciseness: Simplify complex conditional checks.
# 2. Readability: Make code more expressive and easier to understand.
# 3. Performance: Often more efficient than equivalent for loops.
# 4. Flexibility: Work with any iterable, not just lists.

# These functions are particularly useful in:
# - Data validation
# - Filtering operations
# - Conditional logic in list comprehensions
# - Simplifying complex boolean expressions
# They provide a pythonic way to perform checks across collections, enhancing code clarity and efficiency.

## example 1 ##
result = all([True, True, False])
print(f"example 1-1 all: {result}")

result = all([True, True, True])
print(f"example 1-2 all: {result}")

## example 1 ##
result = any([True, True, False])
print(f"example 1-1 any: {result}")

result = any([True, True, True])
print(f"example 1-2 any: {result}")

result = any([False, False, False])
print(f"example 1-2 any: {result}")

# and => all , true and true => true
# or => any , true or false => true

## example 2 ##
nums = [1, 2, 3, 4, 5]
result = all(num > 2 for num in nums)
print(f"example 2-1 all: {result}")

result = any(num > 2 for num in nums)
print(f"example 2-2 any: {result}")

## example 3 ##
nums = [2, 5, 6, 8, 10]
result = all(num % 2 == 0 for num in nums)
print(f"example 3-1 all: {result}")

result = any(num % 2 == 0 for num in nums)
print(f"example 3-2 any: {result}")


## example 4 ##

users = ["john", "jane", "doe", "smith"]
result = all(user[0] == "j" for user in users)
print(f"example 4-1 all: {result}")

result = any(user[0] == "j" for user in users)
print(f"example 4-2 any: {result}")
