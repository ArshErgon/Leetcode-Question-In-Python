




def slidingWindowMaximum(nums, k):
    if len(nums) < k:
        return []

    currentMax = max(nums[:k])
    result = list()
    result.append(currentMax)
    left = 0
    for right in range(k, len(nums)):
        left += 1

        if currentMax == nums[left-1]:
            if nums[left] >= currentMax - 1:
                currentMax = nums[left]
            else:
                currentMax = max(nums[left:right+1])

        currentMax = currentMax if currentMax > nums[right] else nums[right]

        result.append(currentMax)
    
    return result


print(slidingWindowMaximum([1,3,-1,-3,5,3,6,7], 3))