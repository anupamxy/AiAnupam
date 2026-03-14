# build in function in python

# 1. print() function
print("Hello, World!")
# 2. len() function
print(len("Hello, World!"))
# 3. type() function
print(type(42))
# 4. int() function
print(int("123"))
# 5. str() function
print(str(123))
# 6. list() function
print(list("Hello"))
# 7. dict() function
print(dict(a=1, b=2, c=3))
# 8. sum() function
print(sum([1, 2, 3, 4, 5]))
# 9. max() function
print(max([1, 2, 3, 4, 5]))
# 10. min() function
print(min([1, 2, 3, 4, 5]))
# 11. range() function
print(list(range(5)))
# 12. input() function
name = input("Enter your name: ")
print(f"Hello, {name}!")

#13. abs() function
print(abs(-5))
#14. round() function
print(round(3.14159, 2))
#15. sorted() function
print(sorted([5, 2, 9, 1, 5, 6]))
#16. enumerate() function
print(list(enumerate(["a", "b", "c"])))

#17. zip() function
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list(zip(list1, list2)))

#18. map() function
def square(x):
    return x**2
print(list(map(square, [1, 2, 3, 4, 5])))


##output of the above code will be:
#Hello, World!
#13
#<class 'int'>
#123
#123
#['H', 'e', 'l', 'l', 'o']
#{'a': 1, 'b': 2, 'c': 3}
#15
#5
#1
#[0, 1, 2, 3, 4]
#Hello, World!
#13
#<class 'int'>
#123
#123
#['H', 'e', 'l', 'l', 'o']
#{'a': 1, 'b': 2, 'c': 3}
#15
#5
#1
#[0, 1, 2, 3, 4]
#Enter your name: