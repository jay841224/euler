for x in reversed(range(999*999+1)):
    a = 10
    y = x
    goNextStep = True
    haveAnswer = False
    while(y // a >= 10):
        a *= 10   # get number x digit
    r_digit = y % 10
    l_digit = y // a
    if(not r_digit == l_digit ):
        goNextStep = False
        continue
    while(a > 1):
        y = y // 10
        a = a/100
        if(a <= 1):
            break
        r_digit = y % 10
        l_digit = y // a
        l_digit = l_digit % 10
        if(not r_digit == l_digit):
            goNextStep = False
            break
    while(goNextStep):
        y = x
        a = 999
        while(a >= 100):
            z = y % a
            
            if(z == 0 and y/a <=999):
                haveAnswer = True
                break
            else:
                a -= 1

        break
    if(haveAnswer):
        print(x, a, x/a)
        break
            

