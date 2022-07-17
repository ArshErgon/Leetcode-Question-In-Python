


def removeAllVowelsFromString(string):
    newStringList = []
    for i in string:
        if i not in 'aeiou':
            newStringList.append(i)
        
    return ''.join(newStringList)

print((removeAllVowelsFromString('aeiou')))