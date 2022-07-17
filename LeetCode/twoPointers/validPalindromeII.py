class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.validPalindromeOptimal(s)
        return self.validPalindromeOptimalTwo(s)
        # return self.validPalindromeByDict(s)
    
#     O(n) || O(1)
# runtime: 175ms: 53.30%
    def validPalindromeOptimal(self, string):
        if not string:
            return True
        
        left, right = 0, len(string) - 1
        
        while left < right:
            if string[left] != string[right]:
                skipLetterLeft = string[left + 1:right+1]
                skipLetterRight = string[left : right]
                
                return (skipLetterLeft == skipLetterLeft[::-1] or 
                        skipLetterRight == skipLetterRight[::-1])
            
            left += 1
            right -= 1
            
        return True
    
# O(n) || O(1)
# runtime: 152ms 73.35%
    def validPalindromeOptimalTwo(self, string):
        if not string:
            return True

        left, right = 0, len(string) - 1

        while left < right:
            if string[left] != string[right]:
                return (self.reverse(string[left + 1:right+1]) or self.reverse(string[ left:right]))

            left += 1
            right -= 1

        return True

    def reverse(self, string):
        return string == string[::-1]
    
    
#     this code passed 375/400 cases
# O(n) || O(n)
    def validPalindromeByDict(self, string):
        if not string:
            return True

        hashMap = dict()

        for i in string:
            hashMap[i] = 1 + hashMap.get(i, 0)


        oddCount = 0

        for key in hashMap:
            if hashMap[key] % 2 == 1:
                oddCount += 1


        return oddCount <= 2


sol = Solution()
print(sol.validPalindrome("abca"))