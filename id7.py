
def isPrimeGivenSmallerPrimes(num, smallerPrimes):
    for i in smallerPrimes:
        if num % i == 0:
            return False
    return True

smallerPrimes = [2, 3, 5, 7, 11, 13]

i = 14
while len(smallerPrimes) < 10001:
    if isPrimeGivenSmallerPrimes(i, smallerPrimes):
        smallerPrimes.append(i)
    i += 1

print(smallerPrimes[len(smallerPrimes) - 1])
