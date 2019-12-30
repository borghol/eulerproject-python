import math

numbers = [str(x) for x in range(0, 10)]
finalOrder = []
count = 0

while len(numbers) > 0:
    for i in numbers:
        if (math.factorial(len(numbers)-1) + count < 1000000):
            count += math.factorial(len(numbers)-1)
        else:
            numbers.remove(i)
            finalOrder.append(i)
            break

for x in finalOrder:
    print(x, end='')
print()