# mini projectot on exception handling
def get_number():
    while True:
        try:
            num=int(input("Enter a number: "))
            if num<0:
                raise ValueError("Negative number is not allowed.")
            if num==0:
                raise ZeroDivisionError("Zero is not allowed.")
            if num!=int:
                raise TypeError("Invalid input type. Please enter an integer.")
            if num>100:
                raise Exception("Number is too large. Please enter a number less than or equal to 100.")
            print(f"You entered: {num}")
        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            print("This will always execute")
            
    
for _ in range(5):
    get_number()