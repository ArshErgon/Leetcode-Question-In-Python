

# O(n) || O(n)
def twoSums(nums, target):
    seen = dict()
        
    for idx, val in enumerate(nums):
        compliment = target - val
        if compliment in seen:
            return [seen[compliment], idx]
        seen[val] = idx
    return False


# O(n^2) || O(1)
def twoSumBruteForce(nums, target):
    for i in range(len(nums)):
        currNum = nums[i]
        for j in range(i+1, len(nums)):
            nextNum = nums[j]
            if (currNum + nextNum) == target:
                return [i, j]

    
    return [-1, -1]



def twoSumSort(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1

    while left < right:
        if (nums[left] + nums[right]) > target:
            right -= 1
        elif (nums[left] + nums[right]) < target:
            left += 1
        else:
            return [left, right]

    return [-1, -1]
