



def errorMatch(nums):
    if not nums:
        return nums

    result = []

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            result += [nums[i], i + 1]
        
    return result
    


def cyclicSort(array):
    i = 0
    while i < len(array):
        check = array[i] - 1

        if array[i] != array[check]:
            array[i], array[check] = array[check], array[i]
        else:
            i += 1
    
array = [1,2,2,4]

print(errorMatch(array))
