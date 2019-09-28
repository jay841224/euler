import numpy as np
def array_size(size):
    array = np.ones((size  + 2, size + 1))
    x = 1
    y = 1
    while y <= size:
        while x <= size:
            array[y, x] = array[y - 1, x] + array[y, x - 1]
            x += 1
        y += 1
        x = 1

    return array[size, size]

print(array_size(20))