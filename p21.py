#valuate the sum of all the amicable numbers under 10000.
count = 0
def amicable(number):
    a = 2
    local_count = 1
    local_count2 = 1
    while number > a:
        if number % a == 0:
            local_count += a
        a += 1
    a = 2
    while local_count > a:
        if local_count % a == 0:
            local_count2 += a
        a += 1
    if local_count2 == number and not number == local_count:
        return number
    else:
        return 0

for x in range(1, 10000 + 1):
    count += amicable(x)
print(count)

