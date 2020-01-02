sum = 1
multiplier = 2
num = 1

while multiplier + 1 <= 1001:
    for i in range(4):
        num += multiplier
        sum += num
    multiplier += 2

print(sum)
