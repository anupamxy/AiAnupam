  # file error handling is a mechanism to handle errors gracefully in Python. It allows you to catch and handle exceptions (errors) that may occur during the execution of your program, preventing it from crashing and providing a way to respond to the error.
try:
    with open("file.txt","r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
