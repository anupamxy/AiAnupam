# getter and setter in python
class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter method
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    # Setter method
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age must be a positive integer.")

# Example usage
student = Student("Alice", 20)
print(student.get_name())  # Output: Alice
print(student.get_age())   # Output: 20

student.set_name("Bob")
student.set_age(25)
print(student.get_name())  # Output: Bob
print(student.get_age())   # Output: 25