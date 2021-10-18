number_1 = float(input('Enter number 1: '))
number_2 = float(input('Enter number 2: '))
operation = input('Operation: ')

result = None
error = None

if operation == '+':
    result = number_1 + number_2
elif operation == '-':
    result = number_1 - number_2
elif operation == '*':
    result = number_1 * number_2
elif operation == '/':
    if number_2 != 0:
        result = number_1 / number_2
    else:
        error = 'Can not divide by zero!'
else:
    error = 'Operation is invalid!'

if error == None:
    print(result)
else:
    print(error)
