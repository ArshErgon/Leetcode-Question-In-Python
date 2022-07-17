



def smallerNumberThanCurrent(array):
    count = [0] * 102

    for num in array:
        count[num+1] += 1

    for i in range(1, 102):
        count[i] += count[i - 1]

    
    return [count[num] for num in array]


nums = [8,1,2,2,3]
print(smallerNumberThanCurrent(nums))