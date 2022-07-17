




def sortArrayByParity(array):
    if not array: return array
    left, right = 0, len(array) - 1

    while left < right:
        if array[left] % 2 == 0:
            left += 1
        else:
            array[left], array[right] = array[right], array[left]
            right -= 1
       
    return array


print(sortArrayByParity([3,1,2,4]))