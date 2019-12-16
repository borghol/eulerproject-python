fileToRead = open('./textFiles/id13.txt', 'r')
lines = fileToRead.readlines()

sum = 0
for line in lines:
    sum += int(line)

print(sum)