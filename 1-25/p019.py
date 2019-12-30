day = 6
month = 1
year = 1901
totalSundays = 0
while True:
    day += 7
    
    if month in (9, 4, 6, 11) and day > 30:
        day = day - 30
        month += 1
    
    if month == 2:
        if ((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)) and day > 29:
            day = day - 29
            month += 1
        elif not ((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)) and day > 28:
            day = day - 28
            month += 1
    
    if month in (1, 3, 5, 7, 8, 10) and day > 31:
        day = day - 31
        month += 1
    
    if month == 12 and day > 31:
        day = day - 31
        month = 1
        year += 1
    
    if year == 2001:
        print(totalSundays)
        exit(0)
    
    if day == 1:
        totalSundays += 1
