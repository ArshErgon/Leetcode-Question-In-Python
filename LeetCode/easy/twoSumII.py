
class TwoSumII:
    def __init__(self, array, target):
        self.array = array
        self.target = target

    # O(nlogn) || O(1)
    def twoSum(self):
        array = self.array
        target = self.target

        left, right = 0, len(array) - 1

        while left <= right:
            SUM = array[left] + array[right]
            if SUM == target:
                return [left+1, right+1]
            elif SUM < target:
                left += 1
            else:
                right -= 1
                
        return False


# O(N^2) || O(1)
    def twoSumIIByThreeLoops(self):
        if not self.array:return 0
        array = self.array
        target = self.target

        for i in range(len(array)):
            for j in range(i+1, len(array)):
                    SUM = array[i] + array[j]
                    maybe = [i, j]
                    if SUM == target:
                        return maybe
        return False


print(TwoSumII([2, 7, 11, 15], 9).twoSumIIByThreeLoops())
