#Find the next triangle number that is also pentagonal and hexagonal.
import time

def is_Pentagonal_numbers(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    else:
        return False

def is_hexegonal_number(n):
    if (1 + (1 + 8*n)**0.5) % 4 == 0:
        return True
    else:
        return False

def get_triangle_number(n):
    return n*(n + 1)/2

def main():
    answer_out = False
    n = 285
    while not answer_out:
        n += 1
        #取得triangle number
        x = get_triangle_number(n)
        #確認是否為Pentagonal_numbers和hexegonal_number
        if is_Pentagonal_numbers(x):
            if is_hexegonal_number(x):
                answer_out = True
    print(x)

stime = time.time()
if __name__ == '__main__':
    main()
etime = time.time()
print(etime - stime)