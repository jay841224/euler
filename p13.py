#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
f = open('D:\\python challenge\\project_euler\\p13.txt', 'r')
nums = []
ans = 0
for num in f:
    nums.append(int(num))
for x in nums:
    ans += x
ans = str(ans)
print(ans[:10])