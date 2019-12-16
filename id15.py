import math

def gridRoutes(x, y):
    return (math.factorial(x+y) / math.factorial(x)) / math.factorial(y)

print(gridRoutes(20,20))