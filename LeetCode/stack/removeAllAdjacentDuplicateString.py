



def removeAllAdjacentDuplicateString(string, k):
    if not string: return string
    stack = []

    for char in string:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            stack.append([char, 1])

        if stack[-1][1] == k:
            stack.pop()

    
    return ''.join(char*freq for char, freq in stack)


print(removeAllAdjacentDuplicateString('deeedbbcccbdaa', 3))