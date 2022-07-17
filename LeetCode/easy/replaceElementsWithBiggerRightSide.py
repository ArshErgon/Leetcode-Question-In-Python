
# O(N^2) || O(1)
def replaceElementsToTheRight(array):
    if not array:return array
    for i in range(len(array)):
        maxVal = 0
        for j in range(i+1, len(array)):
            maxVal = max(maxVal, array[j])
        array[i] = maxVal

    
    array[-1] = -1

    return array

# O(N) || O(1)
def replaceElementsToTheRight(array):
    if not array:return array
    rightMax = -1
    for i in reversed(range(len(array))):
        newMax = max(rightMax, array[i])
        array[i] = rightMax
        rightMax = newMax
    return array


print(replaceElementsToTheRight([17,18,5,4,6,1]))