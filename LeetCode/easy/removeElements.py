

# O(N) || O(1)
def removeElements(array, n):
    if not array:
        return 0

    i = 0

    for num in array:
        if num != n:
            array[i] = num
            i += 1
    return array[:i]


print(removeElements([0,1,2,2,3,0,4,2], 3))
    