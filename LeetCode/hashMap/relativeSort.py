


# O(n+m) || O(1)
def relativeSort(arrOne, arrTwo):
    count = [0] * 1001
    countingSort(arrOne, count)
    print(count)

    i = 0
    for num in arrTwo:
        while count[num] != 0:
            arrOne[i] = num
            count[num] -= 1
            i += 1
    
    for j in range(len(count)):
        while count[j] != 0:
            arrOne[i] = j
            count[j] -= 1
            i += 1

    return arrOne


def countingSort(arrOne, count):
    for i in arrOne:
        count[i] += 1



arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print(relativeSort(arr1, arr2))
