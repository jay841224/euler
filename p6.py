def abc(number):
    sum = 0
    square = 0
    for x in range(1, number+1):
        square += x**2
        sum += x
    answer = sum**2 - square
    return answer

a = abc(100)
print(a)