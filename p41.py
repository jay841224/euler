#Pandigital prime
import time
from math import sqrt
def is_prime(n):
    a = 2
    while a < sqrt(n):
        if n%a == 0:
            return False
        else:
            a += 1
    return True


def is_Pandigital(n):
    n = list(str(n))
    for x in range(1, 10):
        try:
            n.remove(str(x))
        except:
            return False
        if n == []:
            return True
    return False

def main():
    max = 0
    for x in range(3, 7654321, 2):
        if is_Pandigital(x):
            if is_prime(x):
                max = x
    return max
stime = time.time()
print(main())
etime = time.time()
print(etime - stime)