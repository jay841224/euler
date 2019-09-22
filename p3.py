#What is the largest prime factor of the number 600851475143 ?
def find_prime_factor(number):
    a = 2
    while(number>a):
        if(number%a ==0):
            number = number/a            
        else:
            a += 1
    print(a)
find_prime_factor(600851475143)
