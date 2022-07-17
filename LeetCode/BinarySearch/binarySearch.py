


def binarySearch(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binarySearchByRecursion(array, target):
    if not array:
        return -1

    mid = len(array) // 2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binarySearchByRecursion(array[mid + 1:], target)
    else:
        return binarySearchByRecursion(array[:mid], target)