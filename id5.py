import math

def lcm(a,b):
    gcd = math.gcd(a,b)
    return((abs(a*b)//gcd))

max = 2
for i in range(2,21):
    max=lcm(max,i)

print(max)