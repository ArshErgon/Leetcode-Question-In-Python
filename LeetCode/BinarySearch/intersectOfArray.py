
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         O(n+m) || O(n)
# Runtime: 77ms 47.46% || Memory: 14.2mb 25.50%
        return self.hashMapSol(nums1, nums2)

# O(nlogn), O(nlogm) || O(n)
# Runtime: 93% 24.79% || Memory: 14.1mb 68.42%
        return self.twoPointerSol(nums1, nums2)

# O(nlogn) || O(n)
# Runtime: 56ms 81.21% || Memory:  14.1mb 25.50%
        return self.binarySearch(nums1, nums2)
    
    
    def hashMapSol(self, numOne, numTwo):
        result = []
        numTwoSet = set(numTwo)

        for num in set(numOne):
            if num in numTwoSet:
                result.append(num)
        
        return result


    def twoPointerSol(self, numOne, numTwo):
        numOne.sort()
        numTwo.sort()

        left, right = 0, 0
        result = []
        while left < len(numOne) and right < len(numTwo):
            if numOne[left] < numTwo[right]:
                left += 1
            elif numTwo[right] < numOne[left]:
                right += 1
            else:
                result.append(numOne[left])
                right += 1
                left += 1

            
        return list(set(result))


    def binarySearch(self, numOne, numTwo):
        numTwo.sort()
        result = []
        seen = set()
        for num in numOne:
            if self.binarySearchHelper(numTwo, num) and num not in seen:
                result.append(num)
                seen.add(num)
            seen.add(num)
                
        return result
    
    def binarySearchHelper(self, numOne, num):
        left, right = 0, len(numOne) - 1
        while left <= right:
            mid = (left + right) // 2 

            if numOne[mid] == num:
                return True

            elif numOne[mid] < num:
                left = mid + 1
            else:
                right = mid - 1 


        return False 




sol = Solution()
nums1 = [1]
nums2 = [1]

# print(sol.hashMapSol(nums1, nums2))
# print(sol.twoPointerSol(nums1, nums2))
print(sol.binarySearch(nums1, nums2))