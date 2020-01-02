def isNonTrivialCurious(i, j):
    if i % 10 == 0 or j % 10 == 0:
        return False
    if list(str(i))[0] == list(str(i))[1] or list(str(j))[0] == list(str(j))[1]:
        return False
    for x in range(1, 10):
        if str(x) in list(str(i)) and str(x) in list(str(j)):
            newI = sum([int(k) if int(k) != x else 0 for k in list(str(i))])
            newJ = sum([int(k) if int(k) != x else 0 for k in list(str(j))])
            if newI / newJ == i / j:
                return True
    return False

def multiplyAndReduce(i, j):
    x = (i[0]*j[0], i[1]*j[1])
    upTo = min(x[0], x[1])
    for k in range(2, upTo+1):
        while x[0] % k == 0 and x[1] % k == 0:
            x = (x[0]//k, x[1]//k)
    return x

fractions = []

for i in range(10, 100):
    for j in range(i+1, 100):
        if (isNonTrivialCurious(i, j)):
            fractions.append((i,j))

minFraction = (1, 1)
for f in fractions:
    minFraction = multiplyAndReduce(minFraction, f)

print(minFraction)