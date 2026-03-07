##tuples are immutable lists
a=(1,2,3,4,5)
q,b,c,d,e=a
print(f"q,b,c,d,e:{q,b,c,d,e}")
print(f"Tuple:{a}")
print(f"First element:{a[0]}")
print(f"Last element:{a[-1]}")
print(f"Slice:{a[1:4]}")