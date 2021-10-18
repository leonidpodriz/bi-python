from statistics import mean

print(min([1, 2, 3, 10]))  # 16
print(max([1, 2, 3, 10]))  # 16
print(len([1, 2, 3, 10]))  # 16
print(sum([1, 2, 3, 10]))  # 16
print(mean([1, 2, 3, 10]))  # 16

operations = {
    '+': lambda x, y: x + y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y,
}

number1 = input('n1?')
number2 = input('n2?')
op = input('Op?')

print(operations[op](int(number1), int(number2)))
