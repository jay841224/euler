def is_prime(n):
    
    a = 3
    while a < n:
        if n%a == 0:
            return False
        a += 2
        if a > n**0.5:
            return True
    return False

def repeat(n):
    number = list(str(n))
    number = number[:-1]
    for i in number:
        if number.count(i) >= 3:
            return True
    return False

def main():
    primes = []
    primess = []
    for n in range(100000, 100500):
        if n%10 not in [0, 2, 4, 5, 6, 8]:
            if is_prime(n):
                primes.append(n)
    for n in primes:
        if repeat(n) == False:
            primess.append(n)

    print(primess)

if __name__ == '__main__':
    main()
    