# https://projecteuler.net/problem=4

largestNumber = 999 * 999
smallestNumber = 100 * 100

def isPalindrome(num):
    strNum = str(num)
    if len(strNum) % 2 != 0:
        return False
    return strNum[0:(len(strNum)//2)] == strNum[(len(strNum)//2)::][::-1]

def isProductOfThrees(num):
    for i in range (100, 999):
        if (num % i == 0 and len(str(num // i)) == 3):
            return True
    return False

for i in range(largestNumber,smallestNumber,-1):
    if (isPalindrome(i) and isProductOfThrees(i)):
        print('The largest number is: ' + str(i))
        exit(0)
