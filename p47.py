

def npf(number):
    """function which will return
    the number of prime factors"""
    i = 2
    #set()會刪除相同的數據
    a = set()
    while i < number**0.5 or number == 1:
        if number % i == 0:
            number = number/i
            a.add(i)
            i -= 1
        i += 1
    #回傳len + 1是因為在 i > number**0.5 時會跳出迴圈，而此時number也是prime，因此要+1
    return (len(a)+1)

# iterator
j = 2*3*5*7

# while loop
while True:
    if npf(j) == 4:
        j += 1
        if npf(j) == 4:
            j += 1
            if npf(j) == 4:
                j += 1
                if npf(j) == 4:
                    print(j-3)
                    break
    j += 1


