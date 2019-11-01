from itertools import permutations
def permutation():
    result = 0
    for x in permutations('0123456789'):
        if x[0] == '0':
            continue
        primes = [2, 3, 5, 7, 11, 13, 17]
        x = ''.join(x)
        loop = True
        for y in range(7, 0, -1):
            if int(x[y: y + 3]) % primes[y - 1] != 0:
                loop = False
                break
        if loop:
            result += int(x)
    return result

print(permutation())