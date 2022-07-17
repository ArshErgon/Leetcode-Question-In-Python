


def splitArrayLargestSum(array, m):
    left, right = max(array), sum(array)

    while left < right:
        mid = (left + right) // 2
        if canSplit(array, mid, m):
            right = mid
        else:
            left = mid + 1

    
    return left



def canSplit(array, mid, m):
    countSubArray = 1
    sumSubArray = 0

    for num in array:
        sumSubArray += num

        if sumSubArray > mid:
            sumSubArray = num
            countSubArray += 1
            if countSubArray > m:
                return False


    return True



print(splitArrayLargestSum([7, 2, 5, 10, 8], 2))
print(splitArrayLargestSum([1, 2, 3, 4, 5], 2))
print(splitArrayLargestSum([1, 4, 4], 4))
