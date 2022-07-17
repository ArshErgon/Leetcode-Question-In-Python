



def toLowerCase(string):
    if not string:return string
    letters = []
    for i in string:
        if ord(i) >= 65 and ord(i) <= 90:
            letters.append(chr(ord(i)+32))
        else:
            letters.append(i)
    

        
    return ''.join(letters)



print(toLowerCase("HellO@[]"))