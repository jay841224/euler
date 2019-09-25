#Find the sum of all the primes below two million.
def sum_of_primes(upper):
    ans = 2
    for x in range(3, upper+1, 2):
        a = 2
        while a <= x:
            if x%a == 0:
                break
            else:
                if a**2>x:
                    ans += x
                    break
                else:
                    a += 1
                    
    print('the sum of primes numbers below is {}'.format(ans))

sum_of_primes(2000000)