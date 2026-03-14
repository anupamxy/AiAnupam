# set comprehension is a concise way to create sets in Python. It allows you to generate a new set by applying an expression to each item in an iterable, optionally filtering items based on a condition.
menu={"idly","dosa","vada","poori","paratha"}
# without set comprehension
lengths=set()
for item in menu:
    lengths.add(len(item))
print(lengths)
# with set comprehension
lengths={len(item) for item in menu}
print(lengths)