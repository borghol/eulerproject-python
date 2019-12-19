sum=0
squaredSum=0

for i in range(1, 101):
    sum += i
    squaredSum += i*i

print(sum*sum - squaredSum)