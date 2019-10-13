dic = {'0': 1}
for x in range(1, 10):
    sum = 1
    for y in range(1, x + 1):
        sum *= y
    dic[str(x)] = sum

def Digit_factorials():
    output = 0
    for number in range(10, 2540161):
        ans = 0
        a = list(str(number))
        for x in a:
            ans += dic[x]
        if ans == number:
            output += number
    return output
print(Digit_factorials())