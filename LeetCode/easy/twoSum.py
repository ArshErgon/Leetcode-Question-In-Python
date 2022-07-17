

class TwoSum:
    def __init__(self, array, target):
        self.array = array
        self.target = target

# O(N) || O(N)
    def twoSum(self):
        seen = dict()
        array = self.array
        target = self.target
        for idx, num in enumerate(array):
            if (target - num) in seen:
                return [seen[target - num], idx]
            seen[num] = idx
        return False
    
# O(n^2) || O(1)
    def twoBy2Loops(self):
        array = self.array
        target = self.target
        for i in range(len(array)):
            for j in range(i, len(array)):
                if (array[i] + array[j]) == target:
                    return [i, j]
        return False


print(TwoSum([2, 7, 11, 15], 9).twoSum())
    