


def findAllNumbersDisapperedInArray(array):
    if not array: return array
    # allRange = list(range(min(array), len(array)+1))
    # return list(set(allRange) - set(array))
    return list(set(range(min(array), len(array)+1)) - set(array))

# print(findAllNumbersDisapperedInArray([4,3,2,7,8,2,3,1]))


# print(findAllNumbersDisapperedInArray([4,3,2,7,8,2,3,1]))



def findAllNumbersDisapperedInArray(nums):
    if not nums: return nums

    for num in nums:
        index = abs(num) - 1
        nums[index] = -1 * abs(nums[index])


    return [i+1 for i in range(len(nums)) if nums[i] > 0]

print(findAllNumbersDisapperedInArray([4,3,2,7,8,2,3,1]))
