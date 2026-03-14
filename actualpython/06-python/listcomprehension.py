# list comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable, optionally filtering items based on a condition.
menu=["idly","dosa","vada","poori","paratha"]
# without list comprehension
lengths=[]
for item in menu:
    lengths.append(item)
print(lengths)

# with list comprehension
lengths=[item for item in menu]
print(lengths)
