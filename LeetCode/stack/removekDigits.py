


def removeKDigits(nums, k):
    if not k:
        return nums

    minVal = float('inf')
    maxRemove = float('-inf')
    index = [0, 0]

    for i in range(len(nums)-k+1):
        # minVal = min(minVal, int(nums)-int(nums[i:i+k]))
        if maxRemove < int(nums[i:i+k]):
            maxRemove = int(nums[i:i+k])
            index = [i, i+k]
        # maxRemove = max(maxRemove, int(nums[i:i+k]))

    return  nums[:index[0]] + nums[index[1]:] if nums[:index[0]] + nums[index[1]:] else 0


# print(removeKDigits('1432219', 3))
# print(removeKDigits('10200', 1))


def removeKDigits(nums, k):
    if not k:
        return nums

    stack = []

    for num in nums:
        while stack and stack[-1] > num and k:
            stack.pop()
            k -= 1
        stack.append(num)
    stack = ''.join(stack[:len(stack)-k])
    return str(int(stack)) if stack else "0"


print(removeKDigits('1432219', 3))
print(removeKDigits('10200', 1))
print(removeKDigits('10', 1))
print(removeKDigits('9', 1))