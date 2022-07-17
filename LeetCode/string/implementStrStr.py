
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return self.KMP(haystack, needle)
        return self.withOutKMP(haystack, needle)
    
    
# O(n+m) || O(m) n is main string and m is the substring
# 45ms 41.95%
    def KMP(self, haystack, needle):
        if needle == "": return 0
        lps = [0] * len(needle)
        
        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
        
        i = 0 # ptr for haystack
        j = 0 # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1
    
        #     O(n*m) || O(1); 95.78%
    def withOutKMP(self, haystack, needle):
        if not needle: return 0
        left, right = 0, len(needle)

        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            left, right = left + 1, right + 1

        return -1
        
        