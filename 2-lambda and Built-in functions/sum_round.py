################# sum & round #################
# sum() and round() are built-in Python functions used for numerical operations.

# sum():
# - Purpose: Calculates the sum of all items in an iterable.
# - Usage: Adds up numbers in lists, tuples, or other numeric iterables.
# - Syntax: sum(iterable, start=0)
#   - 'start' is an optional parameter to add a number to the sum.

# Why use sum():
# 1. Simplicity: Easier and more readable than manual addition loops.
# 2. Efficiency: Optimized for performance, especially with large datasets.
# 3. Versatility: Works with various iterable types.

# round():
# - Purpose: Rounds a number to a specified number of decimal places.
# - Usage: Formats numbers for display or rounds calculations.
# - Syntax: round(number, ndigits=None)
#   - 'ndigits' specifies the number of decimal places (default is 0).

# Why use round():
# 1. Precision control: Manages floating-point precision in calculations.
# 2. Display formatting: Presents numbers in a more readable format.
# 3. Rounding operations: Useful in financial calculations, statistics, etc.

# Both functions are commonly used in data processing, financial calculations,
# scientific computing, and general programming tasks where numerical
# operations and formatting are required.

## example 1 ##

numbers = [1, 3, 5, 44, 55, 24]

result = sum(numbers)
print(f"example 1-1 sum: {result}")
result = sum(numbers, 10)
print(f"example 1-2 sum: {result}")

## example 2 ##

products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone", "price": 500},
    {"name": "Tablet", "price": 300},
    {"name": "Monitor", "price": 200},
    {"name": "Mouse", "price": 0},
]

# result = sum([product["price"] for product in products]) ################### Please read the note below
totalPrice = sum([product["price"] for product in products])
print(f"example 2-1 sum: {totalPrice}")

productCount = len([product for product in products if product["price"] > 0])
print(f"example 2-2 sum: {productCount}")

averagePrice = totalPrice / productCount
print(f"example 2-3 sum: {averagePrice}")

# Key differences:

## 1. Memory usage:
# - The first line creates a full list in memory before summing.
# - The second line uses a generator, which yields values one at a time.

## 2. Performance:
# - For large datasets, the generator version is generally more efficient.
# - It doesn't need to create and store the entire list in memory.

## 3. Syntax:
# - List comprehension uses square brackets [].
# - Generator expression doesn't use brackets.

## 4. Use case:
# - List comprehension is better if you need the list for other operations.
# - Generator is preferable when you only need to iterate once, like in sum().

# In most cases, especially with sum(), the generator expression (second line)
# is the preferred approach due to its memory efficiency and performance.

## example 3 ##

result = round(3.84159)
print(f"example 3-1 round: {result}")

result = round(3.14159)
print(f"example 3-1 round: {result}")

result = round(3.14159, 2)
print(f"example 3-2 round: {result}")

result = round(3.14159, 3)
print(f"example 3-3 round: {result}")

result = round(3.14159, 4)
print(f"example 3-4 round: {result}")

