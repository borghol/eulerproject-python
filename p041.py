from itertools import permutations
import math

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def isPrime(num):
    if num < 2: return False
    for i in range(2, math.ceil(math.sqrt(num)) +1):
        if num % i == 0:
            return False
    return True

while len(nums) > 0:
    perms = list(permutations(nums))
    index = len(perms) - 1
    while index >= 0:
        num = int(''.join([str(x) for x in perms[index]]))
        if isPrime(num):
            print(num)
            exit(0)
        index -= 1
    nums.pop()
