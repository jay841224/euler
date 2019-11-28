from time import time
def square(n):
    return n**n

def main():
    ten = 0
    a = 10**9
    b = 10**10
    for x in range(1, 1001):
        s = square(x)
        if s//a == 0:
            ten += s
        else:
            ten += s%b
        if ten//b != 0:
            ten = ten%b
    print(ten)

stime = time()
if __name__ == '__main__':
    main()
etime = time()
print(etime - stime)