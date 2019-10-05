#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

def digit_target(digit):
    end = False
    f1 = 1
    f2 = 1
    count = 2
    while not end:
        f3 = f1 + f2
        count += 1
        if f3 // 10**(digit - 1) >= 1:
            end = True
        else:
            f1 = f2
            f2 = f3
    return count

print(digit_target(1000))
