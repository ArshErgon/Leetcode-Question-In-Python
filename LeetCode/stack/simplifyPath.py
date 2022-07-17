



def simplifyPath(string):
    if not string: return string

    stack = []

    for char in string.split('/'):
        if char in {'', '.'}:
            continue
        elif char in '..':
            if len(stack) != 0: stack.pop()
        
        else:
            stack.append(char)

    
    return '/' + '/'.join(stack)



print(simplifyPath("/../abc//./def/"))

