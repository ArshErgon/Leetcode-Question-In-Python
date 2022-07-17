

def reverseVolwelsInString(string):
    left, right = 0, len(string) - 1
    newString = list(string)
    VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    while left < right:
        while left < right and newString[left] not in VOWELS:
            left += 1
        while right > left and newString[right] not in VOWELS:
            right -= 1

        newString[left], newString[right] = newString[right], newString[left]
        left += 1
        right -= 1

    
    return ''.join(newString)


print(reverseVolwelsInString('leetcode'))
print(reverseVolwelsInString('hello'))