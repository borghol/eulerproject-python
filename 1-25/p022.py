f = open("./textFiles/p022_names.txt")

names = []
lines = f.readlines()
for line in lines:
    tokens = line.split(',')
    for token in tokens:
        token = token.replace('"', '')
        names.append(token)

names.sort()

total = 0
for i in range(0, len(names)):
    sum = 0
    for letter in names[i]:
        sum += ord(letter) - 64
    sum *= (i+1)
    total += sum

print(total)