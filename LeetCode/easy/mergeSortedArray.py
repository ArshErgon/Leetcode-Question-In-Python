

# O(N) || O(1)
def mergeSortedArray(array1, array2, m, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if array1[i] > array2[j]:
            array1[k] = array1[i]
            i -= 1
        else:
            array1[k] = array2[j]
            j -= 1
        k -= 1
    while j >= 0:
        array1[k] = array2[j]
        j -= 1
        k -= 1
    return array1


l1 = [4,0,0,0,0, 0]
l2 = [1, 2, 3, 5, 6]
m = 1
n = 5


# l1 = [1,2,4,5,6,0]
# m = 5
# l2 = [3]
# n = 1

print(mergeSortedArray(l1, l2, m, n))

    