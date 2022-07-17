

class Solution:
    def pivotIndex(self, nums):
        return self.findPivotIndexOptimal(nums)
    
#     O(n) || O(1)
# runtime: 153ms 90.08%
    def findPivotIndexOptimal(self, nums):
        if not nums:
            return nums
        
        leftSum = 0
        totalSum = sum(nums)
        
        for i in range(len(nums)):
            diff = totalSum - nums[i] - leftSum
            
            if diff == leftSum:
                return i
            
            leftSum += nums[i]
            
        return -1
    
    # O(n^3) or O(n^4) || O(1) : TLE 
    def findPivotBruteForce(self, array):
        if not array: return array

        for i in range(len(array)): # O(n)
            for j in range(i + 1, len(array)): #O(n)
                if sum(array[:i]) == sum(array[i + 1:]): #sum is O(n) operation O(n^2)
                    return i
        return -1