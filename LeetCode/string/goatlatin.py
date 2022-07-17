
vowels = {'a', 'e','i','o','u', 'A','E','I','O','U'}


def goatLatin(string):
    sub = "maa"
    newString = string.split()
    i = 0
    for idx, val in enumerate(newString):
        if val[0] in vowels:
            newString[idx] = newString[idx] + sub + ('a' * idx)
        else:
            newString[idx] = newString[idx][1:] + newString[idx][0] + sub + ('a' * idx)
        i += 1
    return ' '.join(newString)


print(goatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
print(goatLatin("The quick brown fox jumped over the lazy dog"))