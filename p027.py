import math

primes = []

def isPrimeGivenPrimes(num, primes):
    if num < 0: return False
    if num in primes: return True
    
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0: 
            return False
    primes.append(num)
    return True

def quadraticEquation(a, b, i):
    return i**2 + a*i + b

maxA = 0
maxB = 0
maxNum = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        if not isPrimeGivenPrimes(quadraticEquation(a,b,maxNum +1), primes):
            continue

        i = 0
        while True:
            if isPrimeGivenPrimes(quadraticEquation(a,b,i), primes):
                i += 1
            else:
                break
        if i > maxNum:
            maxNum = i
            maxA = a
            maxB = b

print(maxA, maxB, maxA*maxB, maxNum)