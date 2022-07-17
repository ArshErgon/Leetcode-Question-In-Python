
class Solution:
#     O(n) || O(1); we are dealing with only 26 letters of english lowercase and 26 letters of english uppercase
    def longestPalindrome(self, s: str) -> int:
        hashMap = dict()
        
        for i in s:
            hashMap[i] = hashMap.get(i, 0) + 1
            
        length = 0
        singleChar = 0
        for key in hashMap:
            if hashMap[key] % 2 == 0:
                length += hashMap[key]
            else:
                length += hashMap[key] - 1
                singleChar = 1
        
        return (length + singleChar)


print(Solution().longestPalindrome('abccccdd'))