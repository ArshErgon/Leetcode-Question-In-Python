


# O(N) || O(1)
def removeDuplicates(array):
    if not array: return array

    i = 0
    for j in range(1, len(array)):
        if array[i] != array[j]:
            i += 1
            array[i] = array[j]


    return array[:i+1]




print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


def removeDuplicates(array):
    if not array: return array
    newNoneDuplicateArray = [array[0]]

    for i in range(1, len(array)):
        if array[i] != newNoneDuplicateArray[-1]:
            newNoneDuplicateArray.append(array[i])

    return newNoneDuplicateArray


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


