


def searchInRotatedArray(array):
    if not array:return array

    left, right = 0, len(array)

    minVal = array[0]

    while left < right:
        mid = (left + right) // 2

        if array[left] <= array[mid]:
            minVal = min(minVal, array[left])
            left = mid + 1
        else:
            right = mid
        
    
    return minVal


print(searchInRotatedArray([3,4,5,1,2]))