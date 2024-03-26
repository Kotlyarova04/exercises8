import functools

a = int(input())
b = int(input())
c = int(input())
print(functools.reduce(lambda x, y: x * y, [x for x in range(a, b + 1) if x ** 0.5 % 1 == 0 and x % c == 0]))
