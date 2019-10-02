#Find the sum of the digits in the number 100!
def stage(number):
    ans = 1
    for x in range(1, number + 1):
        ans *= x
    return ans

def sum_digit(number):
    x = list(str(number))
    ans = 0
    for y in x:
        ans += int(y)
    return ans

a = stage(100)
print(sum_digit(a))