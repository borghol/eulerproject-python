import math

def isPrime(num):
    if num < 2: return False
    for i in range(2, math.ceil(math.sqrt(num)) +1):
        if num % i == 0:
            return False
    return True

primes = [2]

n = 3
found = False

while True:
    if isPrime(n):
        primes.append(n)
    else:
        canBeWritten = False
        for p in primes:
            for x in range(1, n):
                if 2*x**2 + p == n:
                    canBeWritten = True
                    break
                if 2*x**2 + p > n:
                    break
            if canBeWritten:
                break
        if not canBeWritten:
            print(n)
            exit()
    n += 2