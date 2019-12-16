import math

num = str(int(2**1000))
sum = 0
for i in range(0, len(num)):
    sum += int(num[i])

print(sum)
