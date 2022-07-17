

# O(n) || O(n)
def validPalindrome(string):
    if not string:
        return True

    newString = list()
# using a list for string because appending in list is O(1)

    for i in string:
        if i.isalnum():
            newString.append(i.lower())
        
        
    left, right = 0, len(newString) - 1

    while left < right:
        if newString[left] != newString[right]:
            return False
        left += 1
        right -= 1
    return True

# print(validPalindrome("A man, a plan, a canal: Panama"))


# O(n) || O(1)
# worse O(n^2) || O(1)
def validPalindrome(string):
    if not string:
        return True
    l, r = 0, len(string) - 1  

    while l < r:
        while l < r and not alphanum(string[l]):
            l += 1

        while r > l and not alphanum(string[r]):
            r -= 1

        if string[l].lower() != string[r].lower():
            return False
        
        l, r = l + 1, r - 1

    return True

def alphanum(char):
    return ((ord('A') <= ord(char) <= ord('Z')) or
            (ord('a') <= ord(char) <= ord('z')) or
            (ord('0') <= ord(char) <= ord('9')))


print(validPalindrome("A man, a plan, a canal: Panama"))
print(validPalindrome("0P"))
