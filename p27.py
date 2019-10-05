primes = []
def prime(number):
    a = 2
    isprime = True
    while a**2 <= number:
        if number % a == 0:
            isprime = False
            break
        else:
            a += 1
    if not isprime:
        return False
    else:
        return True

def find_primes(number):
    for x in range(1, number + 1):
        a = prime(x)
        if a:
            primes.append(x)
            primes.append(-x)

def count_prime(n1, n2):
    keep = True
    value = -1
    while keep:
        value += 1
        a = value**2 + value*n1 + n2
        if not a in primes:
            keep = False
    return value

max = 0
ans = 0
find_primes(1000)
del primes[0]
del primes[0]
for n1 in range(-999, 1000):
    for n2 in primes:
        a = count_prime(n1, n2)
        if a > max:
            max = a
            ans = n1 * n2
print(ans)