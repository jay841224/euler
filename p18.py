f = open('D:\\python challenge\\project_euler\\p18.txt', 'r')
nums = []
new_nums = []
for num in f:
    num = num.split()
    nums.append(num)
nums = nums[::-1]
count = 0
max_iter = len(nums)
while count < max_iter - 1:
    i = 0
    x = 0
    while x < len(nums[i + 1]):
        a = int(nums[i + 1][x]) + int(nums[i][x])
        b = int(nums[i + 1][x]) + int(nums[i][x + 1])
        if a > b:
            new_nums.append(a)
        else:
            new_nums.append(b)
        x += 1
    del nums[0]
    del nums[0]
    nums.insert(0, new_nums)
    new_nums = []
    count += 1
print(nums)
