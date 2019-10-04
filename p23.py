def sum_of_abundant_numbers(upper):
    abundants = []
    unabundant = 0 #1+2+3
    for x in range(1, upper):
        isabundant = False
        a = 2
        sum_a = 1
        while x > a:
            if x % a == 0:
                sum_a += a
            a += 1
        if sum_a > x:
            abundants.append(x)
        if abundants:
            for a in abundants:
                if x - a in abundants:
                    isabundant = True
                    break
        if not isabundant:
            unabundant += x
    return unabundant

print(sum_of_abundant_numbers(28123))