"""
Tuple - it is immutable collection
"""

example_tuple = 1,
print(example_tuple)
print(type(example_tuple))  # <-- type is a function (class) that returns a class\type of object

# Get item by index
print(example_tuple[0])
print(example_tuple[-1])

key_value_tuple = ('key', 'value')
key, value = key_value_tuple

print(key)
print(value)
