class Solution:
    
    def minCostClimbingStairs(self, cost):
        return self.solTwo(cost)
        # return self.solOneByDpList(cost)

#     O(n) || O(1)
#       72ms 62.89%
    
    def solTwo(self, cost):
        if not cost:
            return 0
        
        current, next = 0, 0
        
        for i in reversed(range(len(cost))):
            current, next = next, min(next, current) + cost[i]
            
        return min(current, next)
    
    
# O(N) || O(N)
#         104ms 21.83%
    def solOneByDpList(self, cost):
        if not cost:
            return 0

        dp = [0] * len(cost)

        dp[0] = cost[0]

        if len(cost) > 1:
            dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-2], dp[i-1])

        return min(dp[-2], dp[-1])


sol = Solution()
print(sol.solOneByDpList([10,15,20]))