class Solution:
    def smallestRangeI(self, nums, k):
        delta = max(nums) - min(nums) - 2 * k
        return delta if delta > -1 else 0


sol = Solution()
print(sol.smallestRangeI([1,3,6], 3))