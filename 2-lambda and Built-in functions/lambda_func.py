###################### lambda ######################
# Lambda functions in Python are small, anonymous functions defined using the lambda keyword. 
# They are used for several reasons:
# 1. Conciseness: Allow for quick function definitions without using the def keyword.
# 2. Inline functionality: Useful for short operations that don't require a full function definition.
# 3. Higher-order functions: Often used with functions like map(), filter(), and reduce().
# Callbacks: Convenient for defining simple callback functions.

# Basic syntax:
# lambda arguments: expression

# Lambda functions are best for:
# - Simple operations
# - One-time use functions
# - Situations where a full function definition is overkill
# They enhance code readability and reduce verbosity for simple functions, 
# especially when used with higher-order functions or as arguments to other functions.

## example 1 ##
def add(a, b):
    return a + b

# Get input, split it
a, b = input("Enter two numbers for add: ").split()

result = add(int(a), int(b))
print(f"example 1 add function: {result}")

# lambda
lambda_add = lambda a, b: a + b
result = lambda_add(int(a), int(b))
print(f"example 1 lambda_add: {result}")

## example 2 ##
def myFunc(n):
    return lambda a: a * n

multiply2 = myFunc(2)
multiply3 = myFunc(3)
result = multiply2(10)
result2 = multiply3(10)

print(f"example 2 multiply2: {result}")
print(f"example 2 multiply3: {result2}")

