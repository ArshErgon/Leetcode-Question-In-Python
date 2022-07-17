


from os import major


def majorityElement(array):
    if not array: return array


    hashMap = dict()
    n = len(array)
    for i in array:
        hashMap[i] = 1 + hashMap.get(i, 0)
        if hashMap[i] > (n//2):
            return i
            

# print(majorityElement([3, 2, 3]))
print(majorityElement([6, 5, 5]))


def majorityElement(array):
    if not array: return array

    majority = array[0]
    count = 1

    for i in range(1, len(array)):
        if count == 0:
            count = 1
            majority = array[i]
        elif majority == array[i]:
            count += 1

        else:
            count -= 1

    return majority


# print(majorityElement([2,2,1,1,1,2,2]))