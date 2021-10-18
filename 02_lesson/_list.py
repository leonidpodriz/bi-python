numbers = [23, 5, 73, 2, 4, 6, 8, 4, 32, 6, 8, 8]
strings = ['a', 'b', 'c']

print(numbers)
numbers.sort()
print(numbers)
print('Length:', len(numbers))

new_list = numbers + strings
print(new_list)

new_list.append('new item')

print(new_list)

del new_list[-1]

print(new_list)

new_list.remove('c')

print(new_list)

print('a' in new_list)
print('h' in new_list)

for number in numbers:
    print('>>>', number ** 2)

for index in range(1000000000000):
    print(index ** 2)
