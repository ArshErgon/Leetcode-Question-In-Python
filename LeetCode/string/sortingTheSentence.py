


def sorthingTheSentence(string):
    newString = [0] * len(string.split())

    for chars in string.split():
        newString[int(chars[-1])-1] = chars[:-1]
    

    return ' '.join(newString)


s = "is2 sentence4 This1 a3"

print(sorthingTheSentence(s))