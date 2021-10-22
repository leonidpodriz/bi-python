operations_dict = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
}


def calculator_of_two(x, y, operation='+'):
    operation_function = operations_dict.get(operation)

    if not operation_function:
        return None

    return operation_function(x, y)


print(calculator_of_two(3, 3))
print(calculator_of_two(3, 3, '+'))
print(calculator_of_two(3, 3, '-'))
print(calculator_of_two(3, 3, '*'))
print(calculator_of_two(3, 3, '/'))
print(calculator_of_two(3, 3, '**'))
