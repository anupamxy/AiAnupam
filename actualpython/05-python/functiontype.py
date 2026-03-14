## function types
## pure function

def pure_function(x, y):
    return x + y


#in pure function, the output is only determined by the input values and has no side effects.
print(pure_function(2,3))

## impure function
total=6
def impure_function(x,y):
    global total
    total+=x+y
    print(total)
    
    
impure_function(2,3)


#in impure function, the output can be influenced by factors other than the input values, such as global variables or external state.


# recurive function

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))


# labda function

square=lambda x:x**2

print(square(5))

# in lambda function, we can create anonymous functions that can be used for short-term purposes without the need for a formal function definition.


