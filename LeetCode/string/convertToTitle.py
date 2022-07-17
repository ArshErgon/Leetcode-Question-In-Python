class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber:
            columnNumber, rem = divmod(columnNumber - 1, 26)
            result.append(chr(rem + ord('A')))
            
        
        return ''.join(reversed(result))


sol = Solution()

print(sol.convertToTitle(27))