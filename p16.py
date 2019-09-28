#What is the sum of the digits of the number 2**1000?
def the_n_power(n):
    x = 2 ** n
    a = 0
    while not x == 0:
        a += x % 10
        x = x // 10
    return a
print(the_n_power(1000))