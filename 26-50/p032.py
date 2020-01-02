def isPandigital(i, j):
    arr = []

    arr.extend(list(str(i)))
    arr.extend(list(str(j)))
    arr.extend(list(str(i*j)))

    if '0' in arr: return False
    counts = [0] * 9

    for x in arr: counts[int(x)-1] += 1

    for x in counts:
        if x != 1:
            return False

    return True

numbers = []

for i in range(1, 10000):
    for j in range (i, 10000):
        if isPandigital(i, j):
            if (i*j not in numbers):
                numbers.append(i*j)

print(numbers)
print(sum(numbers))

# 45228