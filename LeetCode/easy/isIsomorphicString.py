

# O(N) || O(26n) --- O(1)
def isIsomorphicString(stringOne, stringTwo):
    return isomorphic(stringOne) == isomorphic(stringTwo)


def isomorphic(string):
    letterDict = dict()
    ans = str()
    nextChar = 'a'
    for char in string:
        if char not in letterDict:
            letterDict[char] = nextChar

            nextChar = chr(ord(nextChar) + 1)
        
        ans += letterDict[char]

    
    return ans


print(isIsomorphicString('foo', 'bar'))