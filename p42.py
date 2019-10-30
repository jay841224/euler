import time
stime = time.time()
with open('D:\\python challenge\\project_euler\\p42.txt', 'r') as f:
    words = f.read().split(',')
    words = [list(word.strip('\"')) for word in words]
    f.close()
#search for max lenth of name
m = max([len(word) for word in words])
triangles = []
a = 0
c = 1
while a < m*26:
    a = c*(c + 1)/2
    triangles.append(a) 
    c += 1

#contribute dic
vals = {}
letter = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for l in letter:
    vals[l] = letter.index(l) + 1

ans = 0
for word in words:
    if sum([vals[w] for w in word]) in triangles:
        ans += 1
print(ans)
etime = time.time()
print(etime - stime)