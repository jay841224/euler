#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?

def even(number):
    return number / 2
def odd(number):
    return 3 * number + 1
answer = [0, 0]
for x in range(1, 1000000):
    y = x
    count = 1
    end = False
    while not end:
        if y%2 == 0:
            y = even(y)
        else:
            y = odd(y)
        count += 1
        if y == 1:
            end = True
    if count > answer[0]:
        answer = [count, x]
print(answer)