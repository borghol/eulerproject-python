from itertools import permutations

def check_if_multiple(numberList, counts):
    index = counts + 1
    initial = int(''.join([str(x) for x in numberList[0:counts]]))
    theRest = numberList[counts::]

    i = 2
    while len(theRest) > 0:
        nextNumber = initial * i
        numberOfNext = 0
        itWorked = False
        while numberOfNext <= len(theRest) and not itWorked:
            numberOfNext += 1
            nextToCheck = int(''.join([str(x) for x in theRest[0:numberOfNext]])) 
            if nextToCheck == nextNumber:
                itWorked = True
        if itWorked:
            i += 1
            theRest = theRest[numberOfNext::]
        else:
            return False
    return True

numbers = [1,2,3,4,5,6,7,8,9]
perms = list(permutations(numbers))

# print(check_if_multiple([1,9,2,3,8,4,5,7,6], 4))

index = len(perms) - 1
while index >= 0:
    for i in range(1, 9):
        if check_if_multiple(perms[index], i):
            print(int(''.join([str(x) for x in perms[index]])))
            exit(0)
    index -= 1





