


def splitTwoStringsToMakePalindrome(a, b):
    return checkPrefixAndSuffix(a, b, len(a)) or checkPrefixAndSuffix(b, a, len(a))


def checkPrefixAndSuffix(charOne, charTwo, n):
    left, right = 0, n - 1

    while left < n:
        if charOne[left] != charTwo[right]:
            break
    
        left += 1
        right -= 1
    
    aSuffix = charOne[left:right + 1]
    bSuffix = charTwo[left:right + 1]
    
    if (aSuffix == aSuffix[::-1]) or (bSuffix == bSuffix[::-1]):
        return True

    return False

a = "ulacfd"
b = "jizalu"



print(splitTwoStringsToMakePalindrome(a, b))