class Solution:
    def maxProfit(self, prices):
        return self.maxProfitOptimal(prices)
    
        # return self.maxProfitByTwoLoops(prices)
    
#     O(n) || O(1) 1778ms 15.94%
    def maxProfitOptimal(self, prices):
        if not prices:
            return 0
        minVal = prices[0]
        maxVal = float('-inf')
        
        for i in range(1, len(prices)):
            profit = prices[i] - minVal
            maxVal = max(maxVal, profit)
            minVal = min(minVal, prices[i])
            
        return maxVal if maxVal > 0 else 0
    
#     O(N^2) || O(1) TLE
    def maxProfitByTwoLoops(self, prices):
        if not prices:
            return prices
        
        maxVal = float('-inf')
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maxVal = max(maxVal, prices[j] - prices[i])
        
        return maxVal if maxVal > 0 else 0