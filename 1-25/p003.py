# https://projecteuler.net/problem=3
import math

num = 600851475143
largestPrimeFactor = 1

i = 2
while i <= num:
    if (num % i == 0):
        largestPrimeFactor = i
        num /= i
        while (num % i == 0):
            num /= i
    i += 1

print(largestPrimeFactor)


