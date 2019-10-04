#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def permutation(a):
    lenth = len(a)
    p_of_x = 0
    p_of_y = 0
    end = False
    count = 0
    ans = []
    while not end:
        for x in range(lenth - 1, -1, -1):
            if a[x - 1] < a[x]:
                p_of_x = x - 1
                for y in range(lenth - 1, p_of_x, -1):
                    if a[y] > a[p_of_x]:
                        p_of_y = y
                        temp_y = a[p_of_y]
                        a[p_of_y] = a[p_of_x]
                        a[p_of_x] = temp_y
                        c = a[p_of_x + 1:]
                        c.reverse()
                        a[p_of_x + 1:] = c
                        count += 1
                        ans = a
                        if count == 999999:
                            end = True
                        break
                break
    return ans

print(permutation(array))