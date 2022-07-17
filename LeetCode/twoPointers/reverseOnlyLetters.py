


def reverseOnlyLetters(string):
    newString = list(string)
    left, right = 0, len(newString) - 1
    while left < right:
        while left < right and newString[left].isalpha() == False:
            left += 1

        while right > left and newString[right].isalpha() == False:
            right -= 1
        
        newString[left], newString[right] = newString[right], newString[left]

        left += 1
        right -= 1
    
    return ''.join(newString)

print(reverseOnlyLetters("a-bC-dEf-ghIj"))