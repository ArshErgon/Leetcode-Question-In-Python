



class Solution:
    def isPalindrome(self, string: str) -> bool:
        # return self.isPalindromeByList(string)
        return self.isPalindromeOptimal(string)
    
#     O(n) || O(1); worse: runtime: O(n^2)
#     106ms 11.29%
    def isPalindromeOptimal(self, string):
        if not string:
            return True
        
        left, right = 0, len(string) - 1
        while left < right:
            while left < right and not self.isAlphaNum(string[left]):
                left += 1
                
            while right > left and not self.isAlphaNum(string[right]):
                right -= 1
            
            if string[left].lower() != string[right].lower():
                return False
            
            left, right = left + 1, right - 1
            
        return True
            
    def isAlphaNum(self, char):
        return ((ord('A') <= ord(char) <= ord('Z')) or
                (ord('a') <= ord(char) <= ord('z')) or
                (ord('0') <= ord(char) <= ord('9')))

    
#     O(n) || O(n)
# 56ms 70.35%
    def isPalindromeByList(self, string):
        if not string:
            return True
        
        newStringList = list()
        
        for char in string:
            if char.isalnum():
                newStringList.append(char.lower())
                
        
        left, right = 0, len(newStringList) - 1
        
        while left < right:
            if newStringList[left] != newStringList[right]:
                return False
            
            left += 1
            right -= 1
            
        return True


sol = Solution()

s = "A man, a plan, a canal: Panama"

print(sol.isPalindromeOptimal(s))