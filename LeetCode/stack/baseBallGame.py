class Solution:
#     O(n) || O(n); where n is the number of scores
# 52ms 61.18%, memory: 14.1mb 73.54%
    def calPoints(self, ops: List[str]) -> int:
        array = ops
        if not array:
            return 0

        stack = []
        nextPrev, prev = None, None
        for i in array:
            if i[0] == '-' or i.isnumeric():
                stack.append(int(i))
                prev = stack[-1]
                nextPrev = stack[-2] if len(stack) > 1 else None
            elif i == 'C':
                if stack:
                    stack.pop()
                    prev = stack[-1] if stack else None
                    nextPrev = stack[-2] if len(stack) > 1 else None
            elif i == 'D':
                if stack:
                    stack.append(prev * 2)
                    prev = stack[-1]
                    nextPrev = stack[-2] if len(stack) > 1 else None
            elif i == '+':
                if stack:
                    stack.append(nextPrev + prev)
                    prev = stack[-1]
                    nextPrev = stack[-2] if len(stack) > 1 else None

        return sum(stack)