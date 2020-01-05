def getPrimeFactors(num):
    i = 2
    n = num
    pf = []
    while n > 1:
        x = 1
        while n % i == 0:
            n = n // i
            x *= i
        if x > 1: pf.append(x)
        
        if i == 2: i+= 1
        else: i += 2
    return pf

def allDistinct4(arr, arr1, arr2, arr3):
    ln = 4
    if len(arr) != ln or len(arr1) != ln or len(arr2) != ln or len(arr3) != ln:
        return False

    x = arr.copy()
    x.extend(arr1)
    x.extend(arr2)
    x.extend(arr3)
    return len(list(dict.fromkeys(x))) == len(arr) + len(arr1) + len(arr2) + len(arr3)


numPrimes = []
# for p in arr:
#     if p not in numPrimes:
#         numPrimes.append(p)
# return len(numPrimes)

n = getPrimeFactors(2)
n1 = getPrimeFactors(3)
n2 = getPrimeFactors(4)
n3 = getPrimeFactors(5)
i = 3
while True:
    n = n1
    n1 = n2
    n2 = n3
    n3 = getPrimeFactors(i + 3)
    if allDistinct4(n, n1, n2, n3):
        print(i)
        exit(0)
    i += 1

    