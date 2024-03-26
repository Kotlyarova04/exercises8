import json

n = input()
m = json.loads(n)
m.sort(key = lambda x: x[1], reverse = True)
print(m)
