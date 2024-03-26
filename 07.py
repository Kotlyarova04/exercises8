import json

def to_json(func):
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapped

@to_json
def get_name():
  return {'name': 'Polina'}

@to_json
def get_mult(a, b):
    return a * b

print(get_name())
print(get_mult(1,4))
