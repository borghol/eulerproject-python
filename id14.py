# Odd numbers produce the largest chains
# so the closest odd number to 1000000 should produce the longest chain

def getChainCount(num):
    maxChain = 1    
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3*num + 1
        maxChain += 1
    return maxChain+1


maxChain = 1
maxNumber = 1
for i in range(1, 1000000):
    if getChainCount(i) > maxChain:
        maxChain = getChainCount(i)
        maxNumber = i
print (maxNumber, maxChain)