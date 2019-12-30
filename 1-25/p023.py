import math 

def getDivisors(num):
    numbers = []
    for j in range(1, num):
        if num % j == 0:
            numbers.append(j)
    return numbers

def getAbundantNumbers(num):
    numbers = []
    for i in range(1, num+1):
        if sum(getDivisors(i)) > i:
            numbers.append(i)
    return numbers

numbers = getAbundantNumbers(28123)
returned = []

for num in range(0, 28124):
    i = 0
    j = len(numbers)-1
    found = False
    while not found and i <= j:
        if (num == numbers[i] + numbers[j]):
            found = True
        if num < numbers[i] + numbers[j]:
            j -= 1
        if num > numbers[i] + numbers[j]:
            i += 1
    if not found: 
        returned.append(num)

print(sum(returned))