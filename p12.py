#What is the value of the first triangle number to have over five hundred divisors?
def find_divisorOf_triangle(number_divisor):
    i = 2
    number = 1
    divisors_count = 0
    while divisors_count < number_divisor:
        number += i
        i += 1
        a = 2
        x = number
        divisors = []
        while x >= a:
            if x%a == 0:
                x /= a
                divisors.append(a)
            else:
                a += 1
        temp_divisors_count = 1
        while len(divisors) > 0:
            count = divisors.count(divisors[0])
            temp_divisors_count *= (count + 1)
            kill = divisors[0]
            while count > 0:
                divisors.remove(kill)
                count -= 1
        divisors_count = temp_divisors_count
    return number
print(find_divisorOf_triangle(500))
