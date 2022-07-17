



def validParentheses(string):
    opposite = {'}', ']', ')'}
    stack = []
    hashMap = {'{':'}', '[':']', '(':')'}
    for i in string:
        if i in hashMap:
            stack.append(hashMap[i])
        else:
            if not stack or stack.pop() != i:
                return False
        
    return not stack


# print(validParentheses("[()]"))
print(validParentheses('()[]{}'))