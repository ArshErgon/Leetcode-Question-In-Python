

# O(n) || O(n)
def decryptStringFromAlphabet(string):
    
    def toAlpha(value):
        return chr(int(value) + ord('a') - 1)

    end = len(string) - 1

    result = []

    while end >= 0:
        if string[end] == '#':
            result += toAlpha(string[end-2:end])
            end -= 3
        else:
            result += toAlpha(string[end])
            end -= 1

    return ''.join(reversed(result))
            


string = "10#11#12"
print(decryptStringFromAlphabet(string))