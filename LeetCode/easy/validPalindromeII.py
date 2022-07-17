


def validPalindrome(string):
    if not string:
        return True
        
    hashMap = dict()

    for i in string:
        hashMap[i] = 1 + hashMap.get(i, 0)

    
    oddCount = 0

    for key in hashMap:
        if hashMap[key] % 2 == 1:
            oddCount += 1

    
    return oddCount <= 2


# print(validPalindrome("abc"))
# print(validPalindrome("abca"))
# print(validPalindrome("aba"))


def validPalindrome(string):
    if not string:
        return True

    left, right = 0, len(string) - 1

    while left < right:
        if string[left] != string[right]:
            skipLetterLeft = string[left + 1: right + 1]
            skipLetterRight = string[left:right]
            return (skipLetterLeft == skipLetterLeft[::-1] or skipLetterRight == skipLetterRight[::-1])

        left += 1
        right -= 1

    return True

# print(validPalindrome("abc"))



def validPalindrome(string):
    if not string:
        return True

    left, right = 0, len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return (reverse(string[left + 1:right+1]) or reverse(string[ left:right]))

        left += 1
        right -= 1

    return True

def reverse(string):
    return string == string[::-1]


print(validPalindrome('abca'))