import random

number_1 = random.randint(0, 300)  # Generates random integer [0, 300)
number_2 = random.randint(0, 300)  # Generates random integer [0, 300)

# Creating string by pattern: 'number + number ='
result = input(str(number_1) + ' + ' + str(number_2) + ' = ')

# Get correct sum
correct_sum = number_1 + number_2

# Convert integer sum to string and compare two strings
if str(correct_sum) == result:
    print('Correct!')
else:
    print('Incorrect!')
