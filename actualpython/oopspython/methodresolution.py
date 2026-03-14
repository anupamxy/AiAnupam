# method resolution

class A:
    label="Base class"
    
class B(A):
    label="B class label"
class C(B):
    label="C class label"
class D(C,B):
     pass
 
cup=D()
print(cup.label)
print(D.__mro__)  # Print the method resolution order

