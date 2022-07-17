class Solution:
    def nextGreaterElement(self, nums1, nums2):
        return self.nextGreaterElementWithMonotonic(nums1, nums2)
    
#     O(n+m)
# runtime: 75ms 55.99%
    def nextGreaterElementWithMonotonic(self, num1, num2):
        monotonicArray = []
        stack = [-1] * len(num1)
        indexMap = {v:i for i,v in enumerate(num1)}
        for i in num2:
            while len(monotonicArray) > 0 and monotonicArray[-1] < i:
                elementPop = monotonicArray.pop()
                if elementPop in indexMap:
                    stack[indexMap[elementPop]] = i
            monotonicArray.append(i)
        return stack
    
# O(n*m) or say it O(n^2) both are not good.
    def bruteForce(self, num1, num2):
        result = list()
        for i in num1:
            isCross = False
            isChange = False
            for j in num2:
                if j == i:
                    isCross = True

                if isCross and i < j:
                    result.append(j)
                    isChange = True
                    break

            if not isChange:
                result.append(-1)


        return result

sol = Solution()

# print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))
print(sol.bruteForce([4,1,2], [1,3,4,2]))