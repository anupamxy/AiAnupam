number=2
print(f"Number:{id(number)}")

number=12
print(f"Number:{id(number)}")


#numbers are immutable in python.when we change the value of number variable it creates a new object in memory but sets are Mutable in python when we change the value of set variable it does not create a new object in memory but changes the existing object in memory.
my_set={1,2,3}
print(f"set:{id(my_set)}")
print("set before change:",my_set)
my_set.add(4)
print(f"set:{id(my_set)}")
print("set after change:",my_set)


#output
#Number:3000960510288
#Number:3000960510608
#set:3000963249984
#set before change: {1, 2, 3}
#set:3000963249984
#set after change: {1, 2, 3, 4}
# so set point to same memory location but number point to different memory location 