                                
import math

def isPrime(num):
    if num < 2: return False
    if num == 2: return True
    for i in range(2, math.ceil(math.sqrt(num)) +1):
        if num % i == 0:
            return False
    return True

maxCon = 0
maxPrime = 1
primes = [x for x in range(2, 1000000) if isPrime(x)]

for size in range(len(primes), 0, -1):
    start = 0
    if sum(primes[start:start+size]) > 1000000:
        continue
    while start + size < len(primes):
        summ =sum(primes[start:start+size])
        print(start, size, summ)
        if (summ) < 1000000 and isPrime(summ):
            print(sum(primes[start:start+size]), start+size)
            exit()
        start += 1
print(maxPrime, maxCon)