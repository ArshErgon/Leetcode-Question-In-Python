




# O(n^3) or O(n^4) || O(1) : TLE 
def findPivotIndex(array):
    if not array: return array

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if sum(array[:i]) == sum(array[i + 1:]):
                return i
    return -1

# print(findPivotIndex([1,7,3,6,5,6]))
# print(findPivotIndex([2,1,-1]))



def findPivotIndex(array):
    if not array: return array

    leftSum = 0
    totalSum = sum(array)

    for i in range(len(array)):
        diff = totalSum - array[i] - leftSum

        if diff == leftSum:
            return i
        
        leftSum += array[i]

    return -1


print(findPivotIndex([1, 7, 3, 6, 5, 6]))
print(findPivotIndex([2,1,-1]))

