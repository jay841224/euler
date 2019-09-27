f = open('D:\\python challenge\\project_euler\\p13.txt', 'r')
nums = []
ans = 0
for num in f:
    nums.append(int(num))
for x in nums:
    ans += x
ans = str(ans)
print(ans[:10])