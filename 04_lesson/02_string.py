# for name in ["james", "lola", "alexandra"]:
#     print(name.rjust(10, " "))

number_string = ''

while number_string.isdigit() == False:
    number_string = input('Enter a number!')

print('Fine!', int(number_string))

# real_number = float(input('Enter a real number: '))
# print(int(real_number) == real_number)


string = 'hello, WoRld!'
print(string[0].upper() + string[1:])

