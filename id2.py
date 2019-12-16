# https://projecteuler.net/problem=2

def fib(a, b, total):
    nextFib = a + b
    if nextFib > 4000000:
        return total
    if nextFib % 2 == 0:
        total += nextFib
    return fib(b, nextFib, total)
    
print(fib(1, 2, 2))