#Digit cancelling fractions
def Digit_cancelling_fractions():
    ansd = 1
    ansn = 1
    for i in range(1, 10):
        for d in range(1, i):
            for n in range(1, d):
                if (10*i + d)*n == (10*n + i)*d:
                    ansd *= d
                    ansn *= n
    return ansd/ansn
print(Digit_cancelling_fractions())