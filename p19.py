#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
def count_sundays(start, end):
    day = 2
    count = 0
    for y in range(start, end + 1):
        i = 0
        if y % 4 == 0:
            if y % 100 == 0:
                if y % 400 == 0:
                        i = 1
            else:
                i = 1
        months = [31, 28 + i, 31, 30, 31, 30, 31, 31, 30 , 31, 30, 31]
        for m in months:
            day += m
            if day % 7 == 0:
                count += 1
    return count

print(count_sundays(1901, 2000))