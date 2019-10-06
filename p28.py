def sum_of_circle(layer):
    ans = 1
    now = 1
    for x in range(3, layer + 1, 2):
        y = 0
        while y < 4:
            now += x - 1
            ans += now
            y += 1
    return ans
print(sum_of_circle(1001)) 