import json


with open('sw_templates.json', 'w') as f:
    n = input()
    m = json.loads(n)
    json.dump(m, f)
with open('sw_templates.json') as f:
    m = f.read()
    print(m)
    m.sort(key = lambda x: x[1], reverse = True)
    print(m)