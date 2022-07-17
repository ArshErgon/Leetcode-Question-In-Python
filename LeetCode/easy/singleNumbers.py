

def singleNumber(array):
    if not array: return None

    res = 0
    for num in array:
        res ^= num
    return res


print(singleNumber([4,1,2,1,2]))
print(singleNumber([2,2,1]))
print(singleNumber([1]))

# O(n) || O(n) --> Brute force
def singleNumber(array):
    if not array: return array

    hashMap = dict()

    for i in array: 
        hashMap[i] = 1 + hashMap.get(i, 0)


    for key in hashMap:
        if hashMap[key] == 1:return key

    return -1


# O(n^2) || O(1) --> Brute force
def singleNumber(array):
    if not array: return array
    for i in range(len(array)):
        change = 0
        for j in range(len(array)):
            if i == j: continue
            if array[i] == array[j]:
                change = 1
                break
        if change == 0: return array[i]


# print(singleNumber([4,1,2,1,2]))
# print(singleNumber([2,2,1]))
# print(singleNumber([1]))