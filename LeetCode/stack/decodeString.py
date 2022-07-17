
# O(n) || O(m) 
def decodeString(string):
    stack = []
    currentString = str()
    currentNum = 0

    for char in string:
        if char.isdigit(): 
            currentNum = currentNum * 10 + int(char)    
        elif char == '[':
            stack.append(currentString)
            stack.append(currentNum)
            currentString = ''
            currentNum = 0
        elif char == ']':
            num = stack.pop()
            prevString = stack.pop()
            currentString = prevString + num * currentString
        else:
            currentString += char
    
    return currentString
        



# print(decodeString("3[a]2[bc]"))
# print(decodeString("3[a2[c]]"))



def decodeString(string):
    stack = []

    for i in string:
        if i != ']':
            stack.append(i)
        else:
            substring = ''
            while stack and stack[-1] != '[':
                substring = stack.pop() + substring
            stack.pop()

            k = ''
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            
            stack.append(int(k) * substring)

    return ''.join(stack)

print(decodeString("3[a]2[bc]"))
