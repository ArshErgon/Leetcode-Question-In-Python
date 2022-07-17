


class Solution:
    def numberOfLines(self, widths, s):
        newLine = 1
        
        width = 0
        
        for char in s:
            charWidth = widths[ord(char) - ord('a')]
            
            if charWidth + width > 100:
                newLine += 1
                width = 0
                
            width += charWidth
                
        return [newLine, width]        
        

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"

print(Solution().numberOfLines(widths, s))