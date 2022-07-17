class Solution:
#     O(N) || O(1) Runtime: 40ms 68.99ms
    def removeElement(self, nums, val):
        i = 0
        
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i
                
sol = Solution()

print(sol.removeElement([3, 2, 2, 3], 3))