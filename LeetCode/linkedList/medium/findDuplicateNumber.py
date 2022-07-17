

class FindDuplicateNumber:
    def __init__(self, array):
        self.array = array


    def findDuplicateNumber(self, nums):
        def floydCycle(nums):
            slow, fast = nums[0], nums[0]
            while True:
                slow = nums[slow]
                fast = nums[nums[fast]]
                
                if slow == fast:
                    return slow
                
        
        meet = floydCycle(nums)
        start = nums[0]
        while start != meet:
            start = nums[start]
            meet = nums[meet]
        return start


    def findDuplicateNumberBySets(self):
        array = self.array
        if not array:
            return array

        
        seen = set()

        while array:
            num = array.pop()
            if num in seen:
                return num
            seen.add(num)
        return False


print(FindDuplicateNumber([1,3,4,2,8, 1]).findDuplicateNumber())