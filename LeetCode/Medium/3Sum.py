


def threeSum(array):
    if not array: return array
    newList = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                num1, num2, num3 = array[i], array[j], array[k]
                total = (num1 + num2 + num3)
                if total == 0:
                    newList.append([num1, num2, num3])

    return newList



# print(threeSum([-1, 0, 1, 2, -1, -4]))




def threeSum(nums):
    nums.sort()
    n, result = len(nums), []

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]: continue

        target = -nums[i]
        beg, end = i + 1, n - 1

        while beg < end:
            if nums[beg] + nums[end] < target:
                beg += 1
            elif nums[beg] + nums[end] > target:
                end -= 1
            else:
                if len(result) == 0 or result[-1] != (nums[i], nums[beg], nums[end]):
                    result.append((nums[i], nums[beg], nums[end]))
                beg += 1
                end -= 1

        return result


# print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))