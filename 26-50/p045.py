
def getHexagonal(n):
    return n*(2*n - 1)

def isTriangular(n):
    return (-1 + (1 + 8*n)**0.5) % 2 == 0 

def isPentagonal(n):
    return (1 + (1+24*n)**0.5) % 6 == 0

i = 144
while True:
    H = getHexagonal(i)
    if isTriangular(H) and isPentagonal(H):
        print(H)
        exit(0)
    i+= 1