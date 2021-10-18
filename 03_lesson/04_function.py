def is_even(number):
    return number % 2 == 0


def print_dict(dict_to_print):
    for key, value in dict_to_print.items():
        print(key, '==>', value)


print(is_even(5))
print(is_even(6))

print_dict(
    {
        'key': 'value',
        'key1': 'value1',
        'key2': 'value2',
    }
)
