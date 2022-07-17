


# O(nlogn) + O(n^2)  = O(n^2)

def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    result = nums[0] + nums[1] + nums[2]
    for i in range(n-2):
        left, right = i + 1, n - 1
        while left < right:
            sum3 = nums[i] + nums[left] + nums[right]
            if abs(result - target) > abs(sum3 - target):
                result = sum3
            if sum3 == target: return target
            if sum3 > target:
                right -= 1  
            else:
                left += 1 
    return result


print(threeSumClosest([-1, 2, 1, -4], 1))
