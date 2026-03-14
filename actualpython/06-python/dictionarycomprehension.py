# dictionary comprehension is a concise way to create dictionaries in Python. It allows you to generate a new dictionary by applying an expression to each item in an iterable, optionally filtering items based on a condition.
my_item={
    "idly":10,
    "dosa":20,
    "vada":12,
    "poori":15
}
# without dictionary comprehension
lengths={}
for item in my_item:
    lengths[item]=len(item)
print(lengths)
# with dictionary comprehension
lengths={item:len(item) for item in my_item}
print(lengths)