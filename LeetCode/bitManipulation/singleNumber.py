class Solution:
    def singleNumber(self, nums):
        return self.singleNumberOptimal(nums)

    #     O(n) || O(1)
#     runtime: 129ms 97.29%
    def singleNumberOptimal(self, array):
        if not array: return None

        res = 0
        for num in array:
            res ^= num
        return res
    
#     O(n^2) || O(1)
    def singleNumberBruteForceOne(self, array):
        if not array: return array
        for i in range(len(array)):
            change = 0
            for j in range(len(array)):
                if i == j: continue
                if array[i] == array[j]:
                    change = 1
                    break
            if change == 0: return array[i]
            
#     O(n) || O(n)
    def singleNumberBruteForceTwo(self, array):
        if not array: return array

        hashMap = dict()

        for i in array: 
            hashMap[i] = 1 + hashMap.get(i, 0)


        for key in hashMap:
            if hashMap[key] == 1:return key

        return -1