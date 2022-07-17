class Solution:
    # O(n) || O(n)
    def removeDuplicates(self, string: str) -> str:
        stack = []
        
        for i in string:
            change = False
            while stack and stack[-1] == i:
                stack.pop()
                change = True
            if not change:
                stack.append(i)
            
        return ''.join(stack)