###################### sorted() ######################
# The sorted() function in Python is a built-in function used to sort iterable objects. It's used for several reasons:
# 1. Versatility: Can sort various iterable types (lists, tuples, strings, etc.).
# 2. Non-destructive: Creates a new sorted list without modifying the original.
# 3. Customization: Allows custom sorting criteria through key and reverse parameters.
# 4. Stability: Maintains relative order of equal elements.

# Syntax:
# sorted(iterable, key=None, reverse=False)

# Key features:
# 1. Returns a new sorted list from the given iterable.
# 2. key: Optional function to customize sort order.
# 3. reverse: If True, sort in descending order.

# Use cases:
# - Organizing data in a specific order
# - Implementing search and sort algorithms
# - Preparing data for display or further processing
# - Sorting complex objects based on specific attributes

# sorted() is particularly useful when you need a flexible, powerful sorting tool that works across different data types and 
# allows for custom sorting logic. It's a key function for data manipulation and organization in Python.

## example 1 ##

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)
print(f"example 1-1 sorted: {sorted_numbers} \n")

sorted_numbers = sorted(numbers, reverse=True)
print(f"example 1-2 sorted: {sorted_numbers} \n")

## example 2 ##

users = [
    {"username": "user1", "age": 25, "posts": ["post1", "post2", "post3"], "email": "user1@example.com", "tel": "1234567890"},
    {"username": "user2", "age": 30, "posts": ["post4", "post5"], "email": "user2@example.com"},
    {"username": "user3", "age": 25, "posts": ["post6", "post7", "post8", "post9"], "email": "user3@example.com"},
    {"username": "user4", "age": 22, "posts": ["post10", "post11", "post12"]},
]

sorted_users = sorted(users, key=len)
print(f"example 2-1 sorted: {sorted_users} \n")

sorted_users = sorted(users, key=len, reverse=True)
print(f"example 2-2 sorted: {sorted_users} \n")

sorted_users = sorted(users, key=lambda user: user["age"])
print(f"example 2-3 sorted: {sorted_users} \n")

sorted_users = sorted(users, key=lambda user: len(user["posts"]))
print(f"example 2-4 sorted: {sorted_users} \n")

sorted_users = sorted(users, key=lambda user: len(user["posts"]), reverse=True)
print(f"example 2-4 sorted: {sorted_users} \n")

sorted_users = list(map(lambda user : user["username"].upper(), sorted(users, key=lambda user: len(user["posts"]), reverse=True)))
print(f"example 2-4 sorted: {sorted_users} \n")

## example 3 ##

courses = [
    {"title": "Python", "students_count": 20},
    {"title": "Java", "students_count": 15},
    {"title": "C#", "students_count": 10},
    {"title": "JavaScript", "students_count": 27},
    {"title": "C++", "students_count": 13},
    {"title": "C", "students_count": 10},
    {"title": "C", "students_count": 10},
]

sorted_courses = sorted(courses, key=lambda course: course["students_count"])
print(f"example 3-1 sorted: {sorted_courses} \n")

sorted_courses = sorted(courses, key=lambda course: course["students_count"], reverse=True)
print(f"example 3-2 sorted: {sorted_courses} \n")

sorted_courses = list(map(lambda course: course["title"].upper(), sorted(courses, key=lambda course: course["students_count"], reverse=True)))
print(f"example 3-3 sorted: {sorted_courses} \n")
