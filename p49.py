from time import time
def is_prime(n):
    if n%2 == 0:
        return False
    a = 3
    while n > a:
        if n%a == 0:
            return False
        a += 2
        if a > n**0.5:
            return True

def main():
    primes = []
    for i in range(1000, 10000):
        if is_prime(i):
            primes.append(i)
    for x in primes:
        for i in range(primes.index(x) + 1, len(primes)):
            gap = primes[i] - x
            if primes[i] + gap in primes:
                a = sorted(list(str(x)))
                b = sorted(list(str(primes[i])))
                c = sorted(list(str(primes[i] + gap)))
                if a == b and b == c:
                    print('{},{},{}'.format(x, primes[i], primes[i] + gap))

if __name__ == '__main__':
    stime = time()
    main()
    etime = time()
    print(etime - stime)