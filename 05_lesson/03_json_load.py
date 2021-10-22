import json

with open('dump.json') as json_file:
    data = json.load(json_file)

print(data)
