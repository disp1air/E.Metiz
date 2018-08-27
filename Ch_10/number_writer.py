import json

numbers = [2, 4, 7, 11, 17]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)