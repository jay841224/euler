#Pandigital multiples
import time
def have_zero(st):
    if '0' in st:
        return False
    else:
        return True

def Pandigital(n):
    i = 1
    a = ''
    while len(a) < 9:
        st = str(n*i)
        if have_zero(st) == False:
            return 0
        a += st
        i += 1
    if len(a) == 9:
        return int(a)
    else:
        return 0

def ispandigital(n):
    n = list(str(n))
    for x in range(1, 10):
        if not str(x) in n:
            return False
    return True

def main():
    ans = 0
    for x in range(10000):
        a = Pandigital(x)
        if a != 0:
            if ispandigital(a):
                if a > ans:
                    ans = a
    return ans

stime = time.time()
print(main())
etime = time.time()
print(etime - stime)