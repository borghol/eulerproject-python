import math

for c in range(1,1000):
    for a in range(1, c):
        for b in range(1, a):
            if a+b+c == 1000 and (a**2 + b**2) == (c**2):
                print(a * b * c)
                exit(0)
            