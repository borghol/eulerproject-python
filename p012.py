def getNumberOfDivisors(n, i):
    if n==1:
        return 1

    while i<=n:
        if n%i==0:
            l=0
            while n%i==0:
                n=(n//i)
                l+=1
            return (l+1)*getNumberOfDivisors(n,i+1)
        i+=1

i = 1
sum = 0
while True:
    sum += i
    if getNumberOfDivisors(sum, 2) > 500:
        print(sum)
        exit(0)
    i += 1