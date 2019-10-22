#Integer right triangles
import time
def triangle(n):
    count = 0
    x = (n//2) + 1
    for a in range(1, x):
        for b in range(x - a, n - a):
            c = n - a - b
            if a**2 + b**2 == c**2:
                count += 1
    return(count)
             


def main():
    ans = 0
    number = 0
    for x in range(4, 1001):
        max_count = triangle(x)
        if max_count > ans:
            ans = max_count
            number = x
    return number
stime = time.time()
print(main())
etime = time.time()
print(etime - stime)