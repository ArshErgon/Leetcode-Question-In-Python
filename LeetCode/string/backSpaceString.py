

# O(n) || O(n) where n is the string present in string and target
def backspaceString(string, target):
    if not string:return False
    if not target:return False
    stackOne, stackTwo = [], []
    for i in string:
        if i == '#':
            if stackOne:
                stackOne.pop()
        else:
            stackOne.append(i)

    for i in target:
        if i == '#':
            if stackTwo:
                stackTwo.pop()
        else:
            stackTwo.append(i)


    
    return stackOne == stackTwo


# print(backspaceString("ab#c", "ad#c"))
# print(backspaceString("ab##", "c#d#"))



def backSpaceStrings(string, target):
    stringLength = len(string) -1 
    targetLength = len(target) -1

    while stringLength >= 0 or targetLength >= 0:
        skipString = 0
        skipTarget = 0

        while stringLength >= 0:
            if string[stringLength] == '#':
                skipString += 1
                stringLength -= 1
            elif skipString > 0:
                stringLength -= 1
                skipString -= 1
            else:
                break
        
        while targetLength >= 0:
            if target[targetLength] == '#':
                skipTarget += 1
                targetLength -= 1
            elif skipTarget > 0:
                targetLength -= 1
                skipTarget -= 1
            else:
                break
        
        if (stringLength >= 0) != (targetLength >= 0):
            return False
        
        if stringLength >= 0 and targetLength >= 0 and string[stringLength] != target[targetLength]:
            return False
        
        stringLength -= 1
        targetLength -= 1

    return True

print(backSpaceStrings("ab##", "c#d#"))
