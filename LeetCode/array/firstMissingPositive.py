




def firstMissingPositive(nums):
    if not nums:
        return nums

    cyclicSort(nums)
    for i in range(len(nums)):
        if i+1 != nums[i]:
            return i + 1
    return len(nums) + 1

def cyclicSort(nums):
    i = 0
    while i < len(nums):
        check = nums[i] - 1
        if nums[i] < len(nums) and nums[i] > 0 and nums[i] != nums[check]:
            nums[i], nums[check] = nums[check], nums[i]
        else:
            i += 1
    
        
# nums = [3, 4, -1, 1]
# nums = [1,2,0]
# nums = [7,8,9,11,12]
nums = [1]
print(firstMissingPositive(nums))