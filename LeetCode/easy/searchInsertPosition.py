


class SearchInsertPosition:
    def __init__(self, array, target):
        self.array = array
        self.target = target

# O(logN) || O(1)
    def sol1(self):

        if not self.array:
            return 0
        if self.target <= self.array[0]:
            return 0
        if self.target > self.array[-1]:
            return len(self.array)
        if self.target == self.array[-1]:
            return len(self.array) -1

        left, right = 0, len(self.array) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.array[mid] == self.target:
                return mid
            elif self.array[mid] < self.target:
                left = mid + 1
            else:
                right = mid - 1

        return left


# O(n) || O(1)
    def sol2(self):
        if not self.array:
            return 0
        for idx, val in enumerate(self.array):
            if val > self.target:
                return idx
            elif val == self.target:
                return idx

        
        return idx + 1 # if the target is bigger than the last number in the array



obj = SearchInsertPosition([1,3,5,6], 7)

print(obj.sol1())