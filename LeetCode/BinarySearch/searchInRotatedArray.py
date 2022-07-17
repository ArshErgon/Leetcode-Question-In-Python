



def searchRotatedArray(nums, target):
    if not nums:
        return -1

    left, right = 0, len(nums) - 1

    return helper(nums, target, left, right)


def helper(num, target, left, right):
    if left > right:
        return -1
    
    middle = (left + right) // 2

    if num[middle] == target:
        return middle

    if num[left] <= num[middle]:
        if target >= num[left] and target <= num[middle]:
            return helper(num, target, left, middle - 1)
        else:
            return helper(num, target, middle + 1, right)
    
    if target >= num[middle] and target <= num[right]:
        return helper(num, target, middle + 1, right)
    else:
        return helper(num, target, left, middle - 1)

    

nums = [3, 5, 1]

print(searchRotatedArray(nums, 1))