# https://projecteuler.net/problem=1

sum = 0
for i in range (1, 999):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print('The Sum of multiples of 3 and 5 for numbers below 1000 is ' + str(sum))