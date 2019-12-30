
def isPalindrome(num):
    strNum = str(num)
    oddFactor = 0
    if len(strNum) % 2 != 0:
        oddFactor += 1
    return strNum[0:(len(strNum)//2)] == strNum[(len(strNum)//2 + oddFactor)::][::-1]

numbers = []
for i in range (1, 1000000):
    if isPalindrome(i) and isPalindrome(int(str(bin(i))[2::])):
        numbers.append(i)

print(numbers, sum(numbers))