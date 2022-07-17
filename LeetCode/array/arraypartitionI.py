

# O(nlogn) || O(1)
def arrayPartitionI(array):
    if not array:
        return array

    array.sort()
    k = 2
    total = 0
    for i in range(0, len(array), k):
        print(array[i:k+i])
        total += min(array[i:k+i])
    return total

print(arrayPartitionI([6,2,6,5,1,2]))