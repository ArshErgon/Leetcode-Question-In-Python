


def reversePrefixWord(string, letter):

    newString = list(string)

    for idx, val in enumerate(newString):
        if val == letter:
            print(newString[:idx+1])
            newString[:idx+1] = newString[:idx+1][::-1]
            return ''.join(newString)

    return ''.join(newString)


word = "abcdefd"
ch = "d"

print(reversePrefixWord(word, ch))