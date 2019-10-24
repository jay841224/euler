import time
def find_total_digit():
    x = 1
    y = 9
    sum = 0
    out = False
    while not out:
        sum += x * y
        if sum >= 1000000:
            out = True
        else:
            x += 1
            y *= 10
    return len(str(y))

def find_target_value():
    count = 0
    x = 10
    y = 1
    target = 1
    ans = 1
    for i in range(1, 1000000):
        if i//x < 1:
            count += y
        else:
            x *= 10
            y += 1
            count += y
        if count >= target:
            i = str(i)
            ans *= int(i[target - count - 1])
            target *= 10
            if target > 1000000:
                break
    return ans
stime = time.time()
print(find_target_value())
etime = time.time()
print(etime - stime)