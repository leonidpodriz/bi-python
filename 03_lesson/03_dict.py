example_dict = {
    'key 1': {
        'key 2': 'value super',
    },
    'key 2': 'value 2',
}

# dict_to_print['key 1'] ==> {'key 2': 'value super',}
print(example_dict['key 1']['key 2'])

print('key 2' in example_dict)
print('value 2' in example_dict)

print(example_dict.values())
print(example_dict.keys())
print(example_dict.items())

for key, value in example_dict.items():
    print(key, '==>', value)
