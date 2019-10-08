#dp algorithm coin sums
def dp():
    coin = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200
    coins = [1] + [0]*target
    for c in coin:
        for x in range(c, target + 1):
            coins[x] += coins[x - c]
    return coins[target]
print(dp()) 
