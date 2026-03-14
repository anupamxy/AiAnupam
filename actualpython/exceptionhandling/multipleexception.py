# multiple exception
def process_data(data):
    try:
        result = 10 / data
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid data type. Please provide a number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# Test the function with different inputs
process_data(5)  # Valid input
process_data(0)  # ZeroDivisionError
process_data("abc")  # TypeError
