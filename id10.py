def isPrimeGivenSmallerPrimes(num, smallerPrimes):
    for i in smallerPrimes:
        if (num ** 0.5)+1 < i:
            return True
        if num % i == 0:
            return False
    return True

smallerPrimes = [2]
sumOfPrimes = 2

for i in range(3, 2000000, 2):
    if (isPrimeGivenSmallerPrimes(i, smallerPrimes)):
        smallerPrimes.append(i)
        sumOfPrimes += i

print(sumOfPrimes)