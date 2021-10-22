import json

data = {
    'number': 0,
    'boolean': True,
    'string': 'string',
    'none': None,
    'float': 3.14,
    'dictionary': {
        'key': 'value',
    },
    'list': [1, 2, 3, 4],

}

with open('dump.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
