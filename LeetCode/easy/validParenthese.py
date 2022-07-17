

# O(n) || O(n)
def validParentheses(n):
    brackets = {
        '(' : ')',
        '[': ']', 
        '{': '}'
    }
    opposite = {'}', ']', ')'}
    stack = []
    for i in n:
        if i in brackets:
            stack.append(brackets[i])
        elif i in opposite:
            if not stack or stack.pop() != i:
                return False
    
    return len(stack) == 0


print(validParentheses('([{}])'))

