from collections import deque
import time
def isPalindrome(number):
    number = str(number)
    dq = deque(number)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

def binary_isPalindrome(number):
    binary = []
    start = False
    for x in range(19, -1, -1):
        a = number//(2**x)
        if a != 0:
            start = True
            number -= 2**x
        if start == True:
            binary.append(str(a))
            if number == 0:
                for y in range(x):
                    binary.append('0')
                break
    return isPalindrome(''.join(binary))

def main():
    ans = 1
    for a in range(2, 1000001):
        if isPalindrome(a):
            if binary_isPalindrome(a):
                ans += a
    return ans
stime = time.time()
print(main())
etime = time.time()
print(etime - stime)