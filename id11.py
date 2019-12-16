
fileToRead = open('./textFiles/id11.txt', 'r')
lines = fileToRead.readlines()
arr = []
for line in lines:
    arr.append(line.split(' '))

for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        arr[i][j] = int(arr[i][j])

max = 0

for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        if j+3 < len(arr[j]):
            if max < (arr[i][j] * arr[i][j+1] * arr[i][j+2] * arr[i][j+3]):
                max = (arr[i][j] * arr[i][j+1] * arr[i][j+2] * arr[i][j+3])
        elif j-3 >= 0:
            if max < (arr[i][j] * arr[i][j-1] * arr[i][j-2] * arr[i][j-3]):
                max = (arr[i][j] * arr[i][j-1] * arr[i][j-2] * arr[i][j-3])

        if i+3 < len(arr):
            if max < (arr[i][j] * arr[i+1][j] * arr[i+2][j] * arr[i+3][j]):
                max = (arr[i][j] * arr[i+1][j] * arr[i+2][j] * arr[i+3][j])
        elif i-3 >= 0:
            if max < (arr[i][j] * arr[i-1][j] * arr[i-2][j] * arr[i-3][j]):
                max = (arr[i][j] * arr[i-1][j] * arr[i-2][j] * arr[i-3][j])

        if i+3 < len(arr) and j+3 < len(arr[i]):
            if max < (arr[i][j] * arr[i+1][j+1] * arr[i+2][j+2] * arr[i+3][j+3]):
                max = (arr[i][j] * arr[i+1][j+1] * arr[i+2][j+2] * arr[i+3][j+3])
        elif i-3 >= 0 and j-3 >= 0:
            if max < (arr[i][j] * arr[i-1][j-1] * arr[i-2][j-2] * arr[i-3][j-3]):
                max = (arr[i][j] * arr[i-1][j-1] * arr[i-2][j-2] * arr[i-3][j-3])

        if i+3 < len(arr) and j-3 >= 0:
            if max < (arr[i][j] * arr[i+1][j-1] * arr[i+2][j-2] * arr[i+3][j-3]):
                max = (arr[i][j] * arr[i+1][j-1] * arr[i+2][j-2] * arr[i+3][j-3])
        elif i-3 > 0 and j+3 < len(arr[i]):
            if max < (arr[i][j] * arr[i-1][j+1] * arr[i-2][j+2] * arr[i-3][j+3]):
                max = (arr[i][j] * arr[i-1][j+1] * arr[i-2][j+2] * arr[i-3][j+3])

print(max)

