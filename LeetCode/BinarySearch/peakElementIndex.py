


def peakElementIndex(array):
    if not array:return array

    left, right = 0, len(array) - 1
    while left < right:
        mid = (left + right) // 2
        if array[mid] > array[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

print(peakElementIndex([0,10,5,2]))           
                