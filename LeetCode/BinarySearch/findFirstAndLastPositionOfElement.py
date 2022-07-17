

class Solution:
    
    def getFirst(self, nums, target):
        left = 0
        right = len(nums) -1 
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    return mid
                right = mid - 1 
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return -1
    
    def getSecond(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid+1] != target:
                    return mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
 
    def searchRange(self, nums, target):
        first  = self.getFirst(nums, target)
        second = self.getSecond(nums, target)
        
        return [first, second]


sol = Solution()

print(sol.searchRange([5,7,7,8,8,10], 8))