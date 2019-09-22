array = []
for x in range(2, 21):
    tempArray = []
    a = 2
    while(a <= x):
        if(x % a == 0):
            x = x/a
            tempArray.append(a)
        else:
            a += 1
        
    for y in tempArray:
        presense = y in array
        if(presense):
            if(tempArray.count(y)>array.count(y)):
                count = 0
                while(count<array.count(y)):
                    array.remove(y)
                count = 0
                while(count<tempArray.count(y)):
                    array.append(y)
                    count += 1
        else:
            array.append(y)

answer = 1
for x in array:
    answer *= x
print(answer)