

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, cur = nums[0], 0
        for n in nums:
            cur += n
            res = max(res, cur)
            if cur < 0:
                cur = 0
        return res


sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]

print(sol.maxSubArray(nums))