#1634 = 1**4 + 6**4 + 3**4 + 4**4
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
def square(a):
    sum = 0
    for x in a:
        sum += x**5
    return sum

def find():
    sum = 0
    for x in range(2, 355000):
        y = x
        a = []
        while y >= 1:
            r = y%10
            a.append(r)
            y = (y - r) / 10
        if square(a) == x:
            sum += x
    return sum

print(find())