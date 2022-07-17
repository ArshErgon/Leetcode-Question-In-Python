


def findAllDuplicatesNumber(nums):
    if not nums:
        return nums

    
    cyclicSort(nums)

    result = []

    for i in range(len(nums)):
        if (i + 1) != nums[i]:
            result.append(nums[i])

    return result

def cyclicSort(nums):
    i = 0

    while i < len(nums):
        check = nums[i] - 1

        if nums[i] != nums[check]:
            nums[i], nums[check] = nums[check], nums[i]
        else:
            i += 1


nums = [4,3,2,7,8,2,3,1]    
print(findAllDuplicatesNumber(nums))