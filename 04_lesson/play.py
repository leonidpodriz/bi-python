name = input('Enter a name: ')
print('Hello, {name}. Nice to see you!')
print(f'Hello, {name}. Nice to see you!')

print('Hello, {}. Nice to see you!'.format(name))
print('Hello, {name}. Nice to see you!'.format(name=name))
print('Hello, %s. Nice to see you!' % (name,))
print('Hello, %(name)s. Nice to see you!' % {'name': name})
