numberMappings = {
    '0': 0,
    '00': 0,
    '1': 3,
    '2': 3,
    '3': 5,
    '4': 4,
    '5': 4,
    '6': 3,
    '7': 5,
    '8': 5,
    '9': 4,
    '10': 3,
    '11': 6,
    '12': 6,
    '13': 8,
    '14': 8,
    '15': 7,
    '16': 7,
    '17': 9,
    '18': 8,
    '19': 8,
    '20': 6,
    '30': 6,
    '40': 5,
    '50': 5,
    '60': 5,
    '70': 7,
    '80': 6,
    '90': 6
}

total = 0
for i in range(1, 1000):
    num = str(i)
    sum = 0
    if (len(num) == 1):
        sum += numberMappings[num]
    if len(num) == 2:
        if i < 20:
            sum += numberMappings[num]
        else:
            sum += numberMappings[(num[0]+'0')] + numberMappings[num[1]]
    if len(num) == 3:
        sum += numberMappings[num[0]] + 10
        if i < 20:
            sum += numberMappings[num]
        else:
            sum += numberMappings[(num[1]+'0')] + numberMappings[num[2]]
    print(i, sum)
    total += sum
total += numberMappings['1'] + 8

print(total)

