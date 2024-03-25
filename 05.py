from functools import reduce

a = int(input())
b = int(input())
c = int(input())
print(reduce(lambda x, y: x * y, [x for x in range(a, b + 1) if x ** 0.5 % 1 == 0 and x % c == 0]))
