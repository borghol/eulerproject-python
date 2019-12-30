
f = open("./textFiles/p042.txt")
lines = f.readlines()
words = []

for line in lines:
    words.extend(line.split(','))

words = [x[1:len(x)-1] for x in words]
wordValues = []

for word in words:
    value = 0
    for letter in word:
        value += ord(letter) - 64
    wordValues.append(value )

countOfTriangleWords = 0
i = 1
while len(wordValues) > 0:
    t = 0.5 * i * (i + 1)
    countOfTriangleWords += sum([1 if x == t else 0 for x in wordValues])
    wordValues = [x for x in wordValues if x > t]
    i += 1

print(countOfTriangleWords)