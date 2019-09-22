#output 10001st prime number
count = 0 
x = 1
while(count < 10001):
    x += 1
    a = 2
    while(x>a):
        if x%a == 0:
            break
        else:
            a += 1
    if x == a:
        count += 1
    
print(x)