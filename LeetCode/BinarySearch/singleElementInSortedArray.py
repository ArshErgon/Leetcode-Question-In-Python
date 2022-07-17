





def singleNonDuplicate(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0 and nums[mid + 1] == nums[mid]):
            left = mid + 1
        else:
            right = mid
            
    return nums[left]


nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))