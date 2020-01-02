import math

primes = [2]
def isPrimeGivenPrimes(num, primes):
    if num < 0: return False
    if num in primes: return True
    for i in range(2, math.ceil(math.sqrt(num)) +1):
        if num % i == 0: 
            return False
    primes.append(num)
    return True

def isCircularPrime(num, primes):
    nums = [x for x in list(str(num))]
    p = []
    for x in nums:
        nums.insert(0, nums.pop())
        k = int(''.join(nums))
        if not isPrimeGivenPrimes(k, primes) and k not in p:
            return []
        elif k not in p:
            p.append(k)
    return p


numbers = []
for i in range(2, 1000000):
    print(i)
    if (i in numbers):
        continue
    numbers.extend(isCircularPrime(i, primes))

print(numbers, len(numbers))

# 55