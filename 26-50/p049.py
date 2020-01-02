import math
from itertools import permutations

def isPrime(num):
    if num < 2: return False
    for i in range(2, math.ceil(math.sqrt(num)) +1):
        if num % i == 0:
            return False
    return True

def getPrimes(arr):
    x = []
    for p in arr:
        if isPrime(int(''.join([str(n) for n in p]))):
            x.append(p)
    return x
numbers = []
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            for z in range(0, 10):
                nums = [i,j,k,z]
                perms = list(set(permutations(nums)))
                if len(perms) < 3:
                    continue
                primes = getPrimes(perms)
                if (len(primes) < 3):
                    continue
                for l in range(0, len(primes)):
                    for m in range(l+1, len(primes)):
                        for n in range(m+1, len(primes)):
                            n1 = int(''.join([str(x) for x in primes[l]]))
                            n2 = int(''.join([str(x) for x in primes[m]]))
                            n3 = int(''.join([str(x) for x in primes[n]]))
                            if n2-n1 == n3-n2 and n2-n1 > 0:
                                if (n1,n2,n3) not in numbers:
                                    numbers.append((n1,n2,n3))

print(numbers)
