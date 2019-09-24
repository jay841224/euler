#There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.
a = b = c = 0
s = 1000
ans = []
while(a<s/3):
    while(b<s/2):
        c = s - a - b
        if(a<b<c and a**2+b**2==c**2):
            ans.append(a*b*c)
        b += 1
    a += 1
    b = a
 
print(ans)
