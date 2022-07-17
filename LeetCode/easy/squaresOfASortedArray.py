
# O(n) || O(1)

def squaresOfASortedArrayOptimalOne(array):
    if not array: return array

    left, right = 0, len(array) - 1

    while left <= right:
        num1 = abs(array[left])
        num2 = abs(array[right])

        if num1 > num2:
            array[left], array[right] = array[right], array[left]
            array[right] = pow(num1, 2)
            right -= 1
        else:
            array[right] = pow(num2, 2)
            right -= 1

    return array

print(squaresOfASortedArrayOptimalOne([-4,-1,0,3,10]))


# O(n) || O(n)
def squaresOfASortedArrayOptimalTwo(array):
    if not array:
        return 0

    newArray = [0] * len(array)
    left, right = 0, len(array) - 1
    j = len(newArray) - 1

    while left <= right:
        num1 = abs(array[left])
        num2 = abs(array[right])
        if num1 > num2:
            newArray[j] = pow(num1, 2)
            left += 1
        else:
            newArray[j] = pow(num2, 2)
            right -= 1
        j -= 1

    return newArray

# print(squaresOfASortedArrayOptimalTwo([-4,-1,0,3,10]))


# O(nlogn) || O(1)ishh, or you can O(n) if you know some sorting algorithm take help of stack

def squaresOfASortedArrayWithSorting(array):
    if not array: return array

    array = sorted([pow(x, 2) for x in array])
    return array

# print(squaresOfASortedArrayWithSorting([-4,-1,0,3,10]))
