


def rotateArray(nums, k):
    if not nums or not k: return nums
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]
    nums[:] = nums[:k]
    


    return nums

print(rotateArray([1,2,3,4,5,6,7], 3))
print(rotateArray([-1,-100,3,99], 2))