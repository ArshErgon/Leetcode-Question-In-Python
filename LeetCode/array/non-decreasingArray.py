



def nonDecreasingArray(array):
    if not array:
        return array

    
    isChange = False
    for i in range(1, len(array)):
        if array[i-1] < array[i]:
            if isChange and not (array[i-1] < 0 or array[i+1] < 0):
                return False
            isChange = True
    return isChange


print(nonDecreasingArray([-1, 4, 2, 3]))
print(nonDecreasingArray([4,2,3]))
print(nonDecreasingArray([4,2,1]))