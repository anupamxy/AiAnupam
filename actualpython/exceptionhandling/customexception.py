# custom exception is a user defined exception that is created by inheriting the built-in Exception class. It allows you to create your own exceptions that can be raised and handled in your code.



class CustomError(Exception):
    pass
def divide(a,b):
    if b==0:
        raise CustomError("Cannot divide by zero")
    return a/b
try:
    
    result=divide(10,0)
    result1=divide(10,2)
    print(result)
    print(result1)
except CustomError as e:
    print(e)