# python comprehension used to
# 1. create new lists, sets, or dictionaries by applying an expression to each item in an iterable.
# 2. filter items from an iterable based on a condition.
# list comprehension
squares = [x**2 for x in range(10)]
print(squares)
# set comprehension
unique_squares = {x**2 for x in range(10)}
print(unique_squares)
# dictionary comprehension
squared_dict = {x: x**2 for x in range(10)}
print(squared_dict)
# filtering with comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)
