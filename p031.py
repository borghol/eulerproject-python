# Dynamic Programming

#         0   1   2   3   4   5
#     1   1   1   1   1   1   1
#     2   1   1   2   2   3   3
#     5   1   1   2   2   3   4
#     10


target = 200
coins = [1,2,5,10,20,50,100,200]
ways = [0] * (target+1)
    
ways[0] = 1

for coin in coins:
    for index in range(coin, target+1):
        ways[index] += ways[index - coin]

print(ways[200])