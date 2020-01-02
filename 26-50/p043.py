from itertools import permutations

numbers = [1,2,3,4,5,6,7,8,9,0]
numbers = [str(x) for x in numbers]
perms = permutations(numbers)

def hasWeirdProperty(arr):
    if int(''.join(arr[1:4])) % 2 != 0:
        return False
    if int(''.join(arr[2:5])) % 3 != 0:
        return False
    if int(''.join(arr[3:6])) % 5 != 0:
        return False
    if int(''.join(arr[4:7])) % 7 != 0:
        return False
    if int(''.join(arr[5:8])) % 11 != 0:
        return False
    if int(''.join(arr[6:9])) % 13 != 0:
        return False
    if int(''.join(arr[7:10])) % 17 != 0:
        return False
    return True

weirdNums = []
for p in perms:
    if hasWeirdProperty(p):
        weirdNums.append(int(''.join(p)))

print(sum(weirdNums))