


class BinarySearch:

    def binarySearchIterative(self, array, target):
        left, right = 0, len(array) - 1
        while left <= right:
            mid = (left+right) // 2

            maybeNum = array[mid]

            if maybeNum == target:
                return mid
            elif maybeNum > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1 


    def binarySearchByRecursion(self, array, target):
        if not array:
            return -1
        return self.binarySearchHelper(array, target, 0, len(array) - 1)

    
    def binarySearchHelper(self, array, target, left, right):
        if right >= left:
            mid = (left + right) // 2 
            element = array[mid]

            if element == target:
                return mid
            elif element < target:
                return self.binarySearchHelper(array, target, mid + 1, right)
            else:
                return self.binarySearchHelper(array, target, left, mid - 1)
        else:
            return -1

l = [5]
t = 5

sol = BinarySearch()

# print(sol.binarySearchIterative(l, t))
print(sol.binarySearchByRecursion(l, t))