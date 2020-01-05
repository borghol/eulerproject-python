summ = 0
for i in range(1, 1001):
    summ += i**i

num = [x for x in str(summ)]
print(int(''.join(num[len(num)-10::])))