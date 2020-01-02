import math

primes = [2, 3, 5, 7, 11]
def isPrimeGivenPrimes(num, primes):
    if num < 2: return False
    if num in primes: return True
    for p in primes:
        if p > math.ceil(math.sqrt(num)) +1:
            primes.append(num)
            return True
        if num % p == 0:
            return False
    # for i in range(2, math.ceil(math.sqrt(num)) +1):
    #     if num % i == 0: 
    #         return False
    # primes.append(num)
    # return True

i = 11
numbers = []

while len(numbers) < 11:
    # print(i)
    if not isPrimeGivenPrimes(i, primes):
        i += 2
        continue
    listi = list(str(i))
    isPrime = True
    while len(listi) > 1 and isPrime:
        listi.pop()
        if not isPrimeGivenPrimes(int(''.join(listi)), primes):
            isPrime = False
            continue
    listi = list(str(i))
    while len(listi) > 1 and isPrime:
        listi.pop(0)
        if not isPrimeGivenPrimes(int(''.join(listi)), primes):
            isPrime = False
            continue
    if isPrime:
        numbers.append(i)
    i += 2

print(numbers, sum(numbers))