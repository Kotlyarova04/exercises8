a = int(input())
b = int(input())
c = int(input())
d = int(input())
output = list(filter(lambda x: x % c == 0 and x % d == 0, range(a, b + 1)))
print(sum(output))
