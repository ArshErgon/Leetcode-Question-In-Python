




def maximumSubarrayWithMinValue(nums):
    stack = [(-1, 0)]
    ret, runningSum = 0, 0
    nums.append(0)
    for num in nums:
        while stack and stack[-1][0] >= num:
            minValue = stack.pop()[0]
            product = minValue * (runningSum - stack[-1][1])
            ret = max(ret, product)
        
        runningSum += num
        stack.append((num, runningSum))

    return ret % (10**9+7)


print(maximumSubarrayWithMinValue([1,2,3,2]))