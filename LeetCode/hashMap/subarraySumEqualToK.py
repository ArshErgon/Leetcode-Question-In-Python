class Solution:
    def subarraySum(self, nums, k):
        curSum = 0
        hashMap = {0:1}
        res = 0
        
        for i in nums:
            curSum += i
            diff = curSum - k
            
            res += hashMap.get(diff, 0)
        
            hashMap[curSum] = 1 + hashMap.get(curSum, 0)
        return res


sol = Solution()
print(sol.subarraySum([1, 1, 1], 2))