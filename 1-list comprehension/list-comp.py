###################### list comprehension ######################
# List comprehension is a concise and powerful way to create lists in Python. 
# It's used for several reasons:
# 1. Readability: It allows you to create lists in a more readable and compact way.
# 2. Performance: Generally faster than traditional for loops for creating lists.
# 3. Expressiveness: Enables you to combine multiple operations in a single line.
# 4. Flexibility: Can be used to create lists, sets, and dictionaries.

# Basic syntax:
# [expression for item in iterable if condition]

# List comprehensions are particularly useful for:
# - Filtering lists
# - Applying functions to list elements
# - Flattening nested lists
# - Creating new lists based on existing ones
# They're a pythonic way to write more efficient and readable code, especially for simple list creation and transformation tasks.

###################### example 1 ######################
nums = []

for i in range(10):
    nums.append(i)

print(f"example 1 nums: {nums}")

# example 2
nums2 = [i for i in range(10)]

print(f"example 2 nums2: {nums2}")

###################### example 3 ######################

organisation = "BTK Academy"

org_list = [i.upper() for i in organisation]

print(f"example 3 org_list: {org_list}")

###################### Conditionals with list comprehension

#for item in list:
#    if (condition):
#        expression

# [expression for item in list if (condition)]
# example 4
nums3 = range(10)
result = []
for num in nums3:
    if num % 2 == 0:
        result.append(num)
######################  example 5 ######################
nums_list = [i for i in nums3 if i % 2 == 0]
print(f"example 5 nums_list: {nums_list}")
###################### example 6 ######################
nums_list = [i if i % 2 == 0 else "odd" for i in nums3]
print(f"example 6 nums_list: {nums_list}")

###################### example 7 ######################

product_price = [100, 200, 300, 0, 500]
tax = []

for price in product_price:
    if price > 0:
        tax.append(price * 1.20)

print(f"example 7 tax: {tax}")

###################### example 8 ######################
tax = [price * 1.20 if price > 0 else "tax not calculated" for price in product_price]
tax2 = [price * 1.20 for price in product_price if price > 0]
print(f"example 8 tax: {tax}")
print(f"example 8 tax2: {tax2}")

###################### practical study questions ######################
# 1- Create a list of numbers between 1-100 that are divisible by 12.

# 2- Create a list containing the digits in the given text.
# text = "Hello 12345 World" => [1,2,3,4,5]

# 3- Write "Freezing Hazard" for each temperature below 4 degrees in the temperatures list.
# temperatures = [20,15,0,-5,-2] => [20,15,"Freezing Hazard","Freezing Hazard","Freezing Hazard"]

# 4- Print the students with scores above 50 from the students and scores lists in a dict format on the screen.
# students = ["ali","ahmet","canan"]
# scores = [50,60,80]
# => "{'ahmet': 60, 'canan': 80}"

# 5- Rewrite the application written with a for loop using list comprehension.
# result = []
# for x in range(3):
#     for y in range(3):
#         result.append((x,y))
# print(result)

######################  Question 1 ###################### 
selected_numbers = [i for i in range(100) if i % 12 == 0 ]
print(f"Question 1 selected_numbers: {selected_numbers}")

######################  Question 2 ###################### 
text = input("Please enter a text: ")
digits = [int(i) for i in text if i.isdigit()]
print(f"Question 2 digits: {digits}")

######################  Question 3 ###################### 
temperatures = input("Please enter temperatures: ")
try:
    temperatures = [temp if float(temp) > 4 else "Freezing Hazard" for temp in temperatures.split()]
    print(f"Question 3 - Valid temperatures: {temperatures}")
except ValueError:
    print("Question 3 - Please enter valid numbers.")

######################  Question 4 ###################### 
students = ["ali","ahmet","canan"]
scores = [50,60,80]

result = {student:score for student,score in zip(students,scores)}
print(f"Question 4 result: {result}")

######################  Question 5 ###################### 
result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(f"Question 5 result 1: {result}")

result = [(x,y) for x in range(3) for y in range(3)]
print(f"Question 5 result 2: {result}")




