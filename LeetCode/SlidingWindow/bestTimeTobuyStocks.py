

# both solution are O(1) in memory
# 1. is O(n)
# 2. is O(n^2)


def bestTimeToBuyStock(stocks):
    if not stocks: return 0

    maxVal = float('-inf')
    minVal = stocks[0]
    for i in range(1, len(stocks)):
        profit = stocks[i] - minVal
        maxVal = max(maxVal, profit)
        minVal = min(minVal, stocks[i])

    return maxVal if maxVal > 0 else 0


print(bestTimeToBuyStock([7,1,5,3,6,4]))



def maxProfitByTwoLoops(self, prices):
        if not prices:
            return prices
        
        maxVal = float('-inf')
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maxVal = max(maxVal, prices[j] - prices[i])
        
        return maxVal if maxVal > 0 else 0