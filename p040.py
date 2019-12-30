
index = 0
finals = []
num = 1
while index <= 1000000:
    arr = [x for x in str(num)]
    if index < 1 and index + len(arr) >= 1:
        i = 0
        while i < len(arr):
            index += 1
            if index == 1:
                finals.append(arr[i])
            i += 1
    elif index < 10 and index + len(arr) >= 10:
        i = 0
        while i < len(arr):
            index += 1
            if index == 10:
                finals.append(arr[i])
            i += 1
    elif index < 100 and index + len(arr) >= 100:
        i = 0
        while i < len(arr):
            index += 1
            if index == 100:
                finals.append(arr[i])
            i += 1
    elif index < 1000 and index + len(arr) >= 1000:
        i = 0
        while i < len(arr):
            index += 1
            if index == 1000:
                finals.append(arr[i])
            i += 1
    elif index < 10000 and index + len(arr) >= 10000:
        i = 0
        while i < len(arr):
            index += 1
            if index == 10000:
                finals.append(arr[i])
            i += 1
    elif index < 100000 and index + len(arr) >= 100000:
        i = 0
        while i < len(arr):
            index += 1
            if index == 100000:
                finals.append(arr[i])
            i += 1
    elif index < 1000000 and index + len(arr) >= 1000000:
        i = 0
        while i < len(arr):
            index += 1
            if index == 1000000:
                finals.append(arr[i])
            i += 1
    else:
        index += len(arr)
    num += 1

x = 1
for i in finals:
    x *= int(i)
print (x)