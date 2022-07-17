
def minSubArrayLen(nums, target):
        i = 0
        res = len(nums)+1
        for j in range(len(nums)):
            target -= nums[j]
            while target <= 0:
                res = min(res, j-i+1)
                target+=nums[i]
                i+=1
        return res % (len(nums)+1)


print(minSubArrayLen([2,3,1,2,4,3], 7))