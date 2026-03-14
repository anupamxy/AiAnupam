# Generator Functions in Python
# Save memory by generating values on the fly instead of storing them all at once.
# you dod'nt want lazy evaluation of values, you can use list comprehension instead of generator expression.
# generator example
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(5)
for number in counter:
    print(number)
    
# without generator, we would have to create a list of all the numbers up to n, which could consume a lot of memory if n is large. With the generator, we can iterate through the numbers one at a time without storing them all in memory at once.
# example

squares = (x**2 for x in range(1, 6))
for square in squares:
    print(square)