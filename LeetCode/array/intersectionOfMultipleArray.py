






from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return self.solTwo(nums)
    
# Runtime: 95ms 64.64% || memory: 14.2mb 62.57%
# O(n^2) || O(1) you can do argure with this we have taken an array of size 1001
# but we are also returning an array, if you are taking that also as an extra space, this its O(m+n)
# where m is the number of elements present in the array, n is the elements present in the array
# otherwise you can say it O(1), if we aren't count the return 'array' as an extra space


    def solOne(self, nums):
        n = len(nums)
        count = [0] * 1001
        for i in range(len(nums)):
            self.countingSort(nums[i], count)
        
        return [num for num in range(1, 1001) if count[num] >= n]
        
    def countingSort(self, nums, count):
        for i in nums:
            count[i] += 1
        
# O(nlogn) || O(n)
# Runtime: 128ms 26.36% || Memory: 14.4mb 6.60%
    def solTwo(self, nums):
        n = len(nums)
        
        hashMap = {}
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                num = nums[i][j]
                hashMap[num] = hashMap.get(num, 0) + 1
                
        return sorted([key for key in hashMap.keys() if hashMap[key] >= n])