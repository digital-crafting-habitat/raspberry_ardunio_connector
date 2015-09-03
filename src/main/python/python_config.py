import json

with open('../resources/config.json') as json_data_file:
    data = json.load(json_data_file)
print(data)
