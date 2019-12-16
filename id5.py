
num = 0
i = 20

def isDivisible(num, fro, to):
    for i in range(to, fro, -1):
        if num % i != 0:
            return False
    return True

while True:
    if isDivisible(i, 1, 20):
        print("Smallest Number divisible by numbers 1-20: " + i)
        exit(0)
    i += 1