


def nextGreaterElement(nums):
    # Write your code here.
    result = [-1] * len(nums)

    stack = list()

    for i in range(2*len(nums)):
        
        circularIdx = i % len(nums)
        
        while len(stack) > 0 and nums[stack[len(stack)-1]] < nums[circularIdx]:
            top = stack.pop()
            result[top] = nums[circularIdx]

        stack.append(circularIdx)

    return result

print(nextGreaterElement([1,2,1]))