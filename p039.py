import math

counts = [0] * 1001

for a in range(1, 500):
    for b in range(1, 500):
        if int(math.sqrt(a**2 + b**2)) ** 2 == a**2 + b**2:
            if a + b + int(math.sqrt(a**2 + b**2)) <= 1000:
                counts[a + b + int(math.sqrt(a**2 + b**2))] += 1

max = 0
num = 0
i = 1

while i < len(counts):
    if counts[i] > max:
        max = counts[i]
        num = i
    i += 1

print(num, max)