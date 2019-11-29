def is_prime(n):
    if n%2 == 0:
        return False
    a = 3
    while a < n:
        if n%a == 0:
            return False
        a += 2
        if a**2 > n:
            return True


def main():
    sum_primes = 5
    primes = [2, 3]
    x = 5
    while True:
        if is_prime(x):
            sum_primes += x
            if sum_primes > 1000000:
                sum_primes = sum_primes - x
                break
            primes.append(x)
        x += 2
    
    #從較大質數開始減
    if not is_prime(sum_primes):
        temp_sum_primes1 = sum_primes
        primes1 = primes.copy()
        for prime in primes[::-1]:
            if is_prime(temp_sum_primes1 - prime):
                ans1 = temp_sum_primes1 - prime
                primes1.remove(prime)
                break
            else:
                temp_sum_primes1 -= prime
                primes1.remove(prime)

    #從較小質數開始減
    if not is_prime(sum_primes):
        temp_sum_primes2 = sum_primes
        primes2 = primes.copy()
        for prime in primes:
            if is_prime(temp_sum_primes2 - prime):
                ans2 = temp_sum_primes2 - prime
                primes2.remove(prime)
                break
            else:
                temp_sum_primes2 -= prime
                primes2.remove(prime)

    if len(primes1) > len(primes2):
        return ans1
    else:
        return ans2

if __name__ == '__main__':
    print(main())