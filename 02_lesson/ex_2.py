shape = input('Enter a name of shape: ')
area = 0
"""
Take as input two real numbers_set and an op 
(“+” or “-” or “/” or “*”) and calculate the result of the op. 
Watch for division by zero errors!
"""
if shape == 'circle':
    radius = float(input('Enter a radius: '))
    area = 3.14 * radius ** 2
elif shape == 'rectangle':
    side_1 = float(input('Enter a side 1: '))
    side_2 = float(input('Enter a side 2 '))
    area = side_1 * side_2
elif shape == 'square':
    side = float(input('Enter a side: '))
    area = side ** 2
elif shape == 'triangle':
    side = float(input('Enter a side: '))
    h = float(input('Enter a H: '))
    area = (2 * h) / side

print(area)

if area >= 100:
    print('Big')
else:
    print('Small')
