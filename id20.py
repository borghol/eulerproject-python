import math

x = math.factorial(100)
sum = 0
while x > 0:
    sum += x % 10
    x = x // 10

print(sum)
