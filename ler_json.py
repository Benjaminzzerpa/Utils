import json

with open('abc.txt', 'r') as file:
    d1_json = json.read()
    d1_json = json.loads(d1_json)

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)