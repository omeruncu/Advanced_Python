##################### min and max #####################
# min() and max() are built-in functions in Python used to find the minimum and maximum values in an iterable or 
# among multiple arguments. 
# 
# They are used for several reasons:
# 1. Simplicity: Provide an easy way to find extreme values.
# 2. Versatility: Work with various data types and multiple arguments.
# 3. Efficiency: Optimized for performance.
# 4. Customization: Allow custom comparison logic via the key parameter.

# Syntax:
# min(iterable, *[, key, default])
# max(iterable, *[, key, default])

# Key features:
# 1. Can take an iterable or multiple arguments.
# 2. key: Optional function to customize comparison.
# 3. default: Value to return if the iterable is empty.

# Use cases:
# 1. Finding extreme values in datasets
# 2. Implementing comparison-based algorithms
# 3. Data analysis and statistics
# 4. Determining winners or top performers in competitions
# 
# min() and max() are particularly useful for quickly identifying the smallest or largest elements in a collection, 
# whether it's numbers, strings, or custom objects. 
# 
# They simplify common programming tasks and are essential tools in data processing and decision-making algorithms.

## example 1 ##

numbers = [3, 5, 1, 7, 9, 2, 4, 6, 8]
char_list = ["a", "b", "v", "d", "q", "z", "g", "h", "u", "*"]
names = ["John", "Jane", "Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"]

print(f"example 1-1 min: {min(numbers)}")
print(f"example 1-2 min: {min(char_list)}")
print(f"example 1-3 min: {min(names)}")

print(f"example 1-4 max: {max(numbers)}")
print(f"example 1-5 max: {max(char_list)}")
print(f"example 1-6 max: {max(names)}")

## example 2 ##

result1 = min(len(name) for name in names)
print(f"example 2-1 min: {result1}")

result2 = max(len(name) for name in names)
print(f"example 2-2 max: {result2}")

## example 3 ##     
result = min(names, key=lambda x: len(x))
print(f"example 3-1 min: {result, result1}")

result = max(names, key=lambda x: len(x))
print(f"example 3-2 max: {result, result2}")

## example 4 ##

products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone", "price": 500},
    {"name": "Tablet", "price": 300},
    {"name": "Monitor", "price": 200},
]

result = min(products, key=lambda x: x["price"])
print(f"example 4-1 min: {result}")

result = max(products, key=lambda x: x["price"])
print(f"example 4-2 max: {result}")

result = min(products, key=lambda x: x["price"])["name"]
print(f"example 4-3 min: {result}")

result = max(products, key=lambda x: x["price"])["name"]
print(f"example 4-4 max: {result}")