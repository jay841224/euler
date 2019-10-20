#Truncatable primes
from collections import deque
import math
import time
def prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for x in range(2, int(math.sqrt(n) + 1)):
        if n%x == 0:
            return False
    return True


def left_to_right(n):
    dq = deque(n)
    while len(dq) > 1:
        dq.popleft()
        if prime(int(''.join(dq))) == False:
            return False
    return True
def right_to_left(n):
    dq = deque(n)
    while len(dq) > 1:
        dq.pop()
        if not prime(int(''.join(dq))):
            return False
    return True

def main():
    x = 11
    Truncatable_primes = []
    while len(Truncatable_primes) < 11:
        if prime(x):
            if left_to_right(str(x)):
                if right_to_left(str(x)):
                    Truncatable_primes.append(x)
        x += 2
    return Truncatable_primes
stime = time.time()
a = main()
ans =0 
for x in a:
    ans += x
etime = time.time()
print(ans)
print(etime - stime)


