#list are mutable means we can change the eleement of the list
a=[1,2,3,4,5]
a.append(6)



print(f"list:{a}")

a.remove(2)
print(f"list:{a}")
a.extend([7,8,9])
print(f"list:{a}")
a.insert(0,9)
print(f"list:{a}")

a.pop(0)
print(f"list:{a}")
a.reverse()
print(f"list:{a}")
a.sort()
print(f"list:{a}")

print(f"max:{max(a)}")
print(f"min:{min(a)}")


#opeerator overloading
a=[1,2,3]
b=[1.5,2.5,3.5]
c=a+b
d=a*3
print(f"list:{d}")
