class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        if not string: return 0

        left, maxWindow = 0, float('-inf')
        seen = set()
        for right in range(len(string)):
            while string[right] in seen:
                seen.remove(string[left])
                left += 1
            seen.add(string[right]) 
            maxWindow = max(maxWindow,(right - left + 1))

        return maxWindow


sol = Solution()
print(sol.lengthOfLongestSubstring('abcabcbb'))