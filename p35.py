import math
import time

startTime = time.time()

limit = 1000000

def prime(n):
    loop = 0
    number_length = len(str(n))

    circle_number = []
    for i in str(n):
        circle_number.append(i)

    while loop != number_length:
        number = int("".join(circle_number))
        for digit in range(2, int(math.sqrt(number)+1)):
            if number % digit == 0:
                return False
        circle_number.append(circle_number[0])
        circle_number.pop(0)
        loop += 1
    return True

def main():
    circular_primes = [2]

    for i in range(3, limit, 2):
        if prime(i):
            circular_primes.append(i)

    print(len(circular_primes))
    print(time.time() - startTime, "seconds")

main()