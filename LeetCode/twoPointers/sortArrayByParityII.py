


def sortArrayByParityII(array):
    if not array:
        return array

    even, odd = 0, 1 
    while even < len(array) and odd < len(array):
        while even < len(array) and array[even] % 2 == 0:
            even += 2
        
        while odd < len(array) and array[odd] % 2 != 0:
            odd += 2
        
        if odd < len(array) and even < len(array):
            array[even], array[odd] = array[odd], array[even]
        even += 2
        odd += 2

    return array


print(sortArrayByParityII([4,2,5,7]))
