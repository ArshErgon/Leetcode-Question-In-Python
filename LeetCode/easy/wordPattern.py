

# O(n+m) runtime;
# O(n+m) space; where n is the string present in pattern 
# and m is the string present in the string
def wordPattern(pattern, string):
    patternMap = dict()
    stringMap = dict()

    stringList = string.split(" ")
    if len(stringList) != len(pattern):
        return False

    
    for char, word in zip(pattern, stringList):
        if char in patternMap and patternMap[char] != word:
            return False
        if word in stringMap and stringMap[word] != char:
            return False
    
        patternMap[char] = word
        stringMap[word] = char

    return True
    

print(wordPattern('abba', "dog cat cat dog"))
# print(wordPattern("aba", "cat cat cat dog"))
    
"aba"
"cat cat cat dog"