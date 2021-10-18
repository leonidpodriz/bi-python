"""
Set - is unordered collections of unique values
"""

colors = {'green', 'white', 'yellow', 'orange', 'green'}  # <-- 'green' duplicates twice

print(colors)  # <-- green saved just once

# Check is element in set
print('red' in colors)
print('white' not in colors)

# Add new elements
colors.add('red')
colors.add('red')
colors.add('red')
colors.add('red')
colors.add('red')
colors.add('red')
colors.add('red')
print(colors)

# Create set from iterable element
numbers_set = set(list([1, 2, 2, 3]))
print(numbers_set)

# And create list from set
numbers_list = list({1, 2, 3})
print(numbers_list)

print({1, 2, 3}.union({3, 4, 5}))  # In A Or B
print({1, 2, 3}.intersection({3, 4, 5}))  # In A and B
print({1, 2, 3}.difference({3, 4, 5}))  # In A and not in B
print({1, 2, 3} - {3, 4, 5})  # Same as difference
print({1, 2, 3}.symmetric_difference({3, 4, 5}))  # In A or B but not both
