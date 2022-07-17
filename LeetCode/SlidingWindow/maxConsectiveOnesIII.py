

# O(n) || O(1)
def maxConsectiveOnesIII(nums, k):
    if not nums:
        return nums

    left, right = 0, 0

    maxWindow = float('-inf')

    while left < len(nums):
        if nums[left] == 0:
            k -= 1
        
        if k < 0:
            if nums[right] == 0:
                k += 1
            right += 1
        
        
        left += 1
     

        maxWindow = max(maxWindow, (left - right))

    return maxWindow


print(maxConsectiveOnesIII([1,1,1,0,0,0,1,1,1,1,0], 2))
# print(maxConsectiveOnesIII([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))