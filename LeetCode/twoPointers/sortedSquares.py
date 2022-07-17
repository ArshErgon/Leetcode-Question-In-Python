class Solution:
    def sortedSquares(self, nums):
        # return self.squaresOfASortedArrayOptimalOne(nums)
        # return self.squaresOfASortedArrayOptimalTwo(nums)
        return self.squaresOfASortedArrayWithSorting(nums)

    #     O(n) || O(1) inplace
#     Runtime: 
    def squaresOfASortedArrayOptimalOne(self, array):
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
    

    # O(n) || O(n)
#     runtime: 344ms 36.34%
    def squaresOfASortedArrayOptimalTwo(self, array):
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

    #     O(nlogn) || O(1)
#     runtime: 352ms 34.00%
    def squaresOfASortedArrayWithSorting(self, array):
        if not array: return array

        array = sorted([pow(x, 2) for x in array])
        return array