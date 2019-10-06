

def integer_combinations(a, b):
    box = []
    for x in range(2, a + 1):
        for y in range(2, b + 1):
            temp = x**y
            if not temp in box:
                box.append(temp)
    return len(box)
print(integer_combinations(100, 100))