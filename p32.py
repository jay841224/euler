Pandigital = []
for x in range(1, 100):
    for y in range(1, 10000//x):
        s = sorted(str(x) + str(y) + str(x*y))
        if s == list('123456789'):
            if not x*y in Pandigital:
                Pandigital.append(x*y)
print(sum(Pandigital))