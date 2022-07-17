



# O(logn) || O(1)
def infiniteArray(array, target):
    left, right = 0, 1
    return helper(array, target, left, right)


def helper(array, target, left, right):

    isTrue = False
    while not isTrue:
        canFindHere = array[left] <= target < array[right]
        if canFindHere:
            while left <= right:
                mid = (left + right) // 2
                if array[mid] == target:
                    return mid
                elif array[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        if array[left] > target:
            isTrue = True
        
        left, right = right, right * 2

    
    return -1



num = list(range(1, 100))
print(infiniteArray(num, 20))