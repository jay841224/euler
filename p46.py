from math import sqrt

def is_prime(n):
    a = 2
    while n > a:
        if n%a == 0:
            return False
        a += 1
        if a > n**0.5:
            return True

def main():
    number = 3
    primes = [2]
    answer = False
    while True:
        if is_prime(number):
            primes.append(number)
        
        else:
            for prime in primes:
                if sqrt((number - prime)/2) - int(sqrt((number - prime)/2)) == 0:
                    break
                if primes.index(prime) == len(primes) - 1:
                    answer = True
                    break
        if answer:
            print(number)
            break
        else:
            number += 2

if __name__ == '__main__':
    main()