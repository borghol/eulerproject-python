def is_pentagonal(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False

def getPentagonal(n):
    return n * (3*n - 1) / 2

diff = 1
# found = False

maxi = 5000
pentagonals = []

i = 1
while len(pentagonals) < maxi:
    pentagonals.append(getPentagonal(i))

print(is_pentagonal(2167 + 1020) and is_pentagonal(2167 - 1020))
exit(0)


while diff < len(pentagonals):
    i = 0
    while i + diff < len(pentagonals):
        print(i, diff)
        if is_pentagonal(pentagonals[i] + pentagonals[i+diff]) and is_pentagonal(pentagonals[i+diff] - pentagonals[i]):
            print(pentagonals[i+diff] - pentagonals[i])
            exit(0)
        i += 1
    diff += 1

