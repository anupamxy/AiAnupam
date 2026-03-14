# raise your own error
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise ValueError("Age must be at least 18.")
    elif age != int:
        raise TypeError("Age must be an integer.")
    else:
        print("Age is valid.")
        
# Test the function with different inputs
try:
    validate_age(-5)  # This will raise a ValueError for negative age
except ValueError as e:
    print(e)

try:
    validate_age(15)  # This will raise a ValueError for age less than 18
except ValueError as e:
    print(e)

try:
    validate_age(25)  # This will print "Age is valid."
except ValueError as e:
    print(e)