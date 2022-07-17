
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return self.binarySearchOptimal(num)
        return self.bruteForce(num)
    
#     O(logN) || O(1)
# runtime: 33ms 81.46%
# memory: 13.8mb 56.48%
    def binarySearchOptimal(self, num):
        if not num:return False
        
        left, right = 0, num + 1
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid # mid** 2 # pow(mid, 2)
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1
    
#     O(n) || O(1)
# runtime: 68ms 9.28%
    def bruteForce(self, num):
        if not num:
            return False
        
        for i in range(1, num+1):
            square = i * i 
            if square == num:
                return True
            elif square > num:
                return False
            
        return -1
    
    