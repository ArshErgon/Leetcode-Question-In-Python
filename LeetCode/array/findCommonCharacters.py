

# O(n^2) || O(n)
def findCommonCharacters(string):
    if not string: return string

    oldList = list(string[0])
    for i in string[1:]:
        newList = []
        for j in i:
            if j in oldList:
                newList.append(j)
        oldList = newList
    
    return newList

print(findCommonCharacters(["bella","label","roller"]))