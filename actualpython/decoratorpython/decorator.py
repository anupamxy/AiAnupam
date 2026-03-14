# decorator in python is a design pattern that allows you to modify the behavior of a function or class method without changing its source code. Decorators are often used to add functionality to existing code in a clean and reusable way.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")
    
say_hello()
    
# using wraps from functools to preserve the original function's metadata
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")
say_hello("Alice")