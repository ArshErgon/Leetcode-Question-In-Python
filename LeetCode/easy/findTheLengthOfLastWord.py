




def lengthofLastWord(string):
    return len(string.split()[-1])


def lengthOfLastWord(string):
    if not string:
        return 0

    i = len(string) - 1
    length = 0

    while string[i] == ' ':
        i -= 1
    
    while i >= 0 and string[i] != ' ':
        length += 1
        i -= 1
    
    return length