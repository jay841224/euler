#What is the value of the first triangle number to have over five hundred divisors?
def triangle_numberOf_divisors(divisor_amount):
    number = 3
    i = 3
    count_divisor = 2
    a_2 = 0
    while count_divisor<divisor_amount:
        a = 2
        count_divisor = 2
        while number > a:
            if number%a == 0:
                if a_2 == number:
                    count_divisor += 1
                else:
                    count_divisor += 2
            a += 1
            a_2 = a**2
            if a_2 > number:
                break
        number += i
        i += 1
    return number
ans = triangle_numberOf_divisors(500)
print(ans)