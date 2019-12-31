def is_pentagonal(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False

def getPentagonal(n):
    return n * (3*n - 1) / 2

i = 1
found = False

while not found:
    for j in range (i-1, 0, -1):
        n = getPentagonal(i)
        m = getPentagonal(j)
        if (is_pentagonal(n+m) and is_pentagonal(n-m)):
            print(i, j, getPentagonal(i) - getPentagonal(j))
            exit(0)
    i += 1