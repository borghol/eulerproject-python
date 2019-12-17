amicableNumbers = []
divisors = []

def getSumOfDivisors(x, divisors):
    for div in divisors:
        if div[0] == x:
            return div[1]
    sumOfDivisors = 0
    for i in range(1, x):
        if x % i == 0:
            sumOfDivisors += i

    divisors.append((x, sumOfDivisors))
    return sumOfDivisors


for i in range(1, 10000):
    divisorSum = getSumOfDivisors(i, divisors)
    if (i != divisorSum and i == getSumOfDivisors(divisorSum, divisors)):        
            amicableNumbers.append(i)
            amicableNumbers.append(divisorSum)

amicableNumbers.sort()
i = 0
while i < len(amicableNumbers)-1:
    if amicableNumbers[i] == amicableNumbers[i+1]:
        amicableNumbers.remove(amicableNumbers[i])
        continue
    i += 1

sum = 0
for x in amicableNumbers:
    sum += x

print (sum)