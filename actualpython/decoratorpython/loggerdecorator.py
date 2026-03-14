# logger using decorator is a common use case for decorators in Python. A logger decorator can be used to log the execution of a function, including its arguments and return value. Here's an example of a simple logger decorator:

from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)