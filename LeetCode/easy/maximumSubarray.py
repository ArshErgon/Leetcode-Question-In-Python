

class MaximumSubarray:
    def __init__(self, array):
        self.array = array

# O(n) || O1
    def solWithOneLoop(self):
        if not self.array:
            return 0

        maxVal = 0
        array = self.array
        res = array[0]
        for i in array:
            maxVal += i
            if maxVal > res:
                res = maxVal
            if maxVal < 0:
                maxVal = 0

        return res
# O(N^2) || O(1)
    def solWithTwoLoops(self):
        maxVal = float('-inf')
        array = self.array 
        for i in range(len(array)):
            for j in range(i, len(array)):
                maxVal = max(maxVal, sum(array[i:j+1]))
        
        return maxVal

print(MaximumSubarray([-2,1,-3,4,-1,2,1,-5,4]).solWithTwoLoops())
print(MaximumSubarray([-2,1,-3,4,-1,2,1,-5,4]).solWithOneLoop())