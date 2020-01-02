import math

numbers = []
for i in range(3, 2540160):
    if sum([math.factorial(int(x)) for x in list(str(i))]) == i:
        numbers.append(i)

print(sum(numbers))
