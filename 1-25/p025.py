# Cannot use recursion because it is too deep to work
def fib():
    xMinus1 = 1
    xMinus2 = 1
    index = 2
    while (len(str(xMinus1 + xMinus2)) < 1000):
        nextNum = xMinus1 + xMinus2
        xMinus2 = xMinus1
        xMinus1 = nextNum
        index += 1
        print(len(str(nextNum)),index)
    return index+1

print(fib())