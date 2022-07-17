




def mergeStringsAlternately(wordOne, wordTwo):
    newString = [''] * (len(wordOne) + len(wordTwo))
    left, right = 0, 0
    indexOne, indexTwo = 0, 1
    while left < len(wordOne) or right < len(wordTwo):
        if len(wordOne) > left:
            newString[indexOne] = wordOne[left]
            indexOne += 2 if right < len(wordTwo) else 1
            left += 1
        if len(wordTwo) > right:
            newString[indexTwo] = wordTwo[right]
            indexTwo += 2 if left < len(wordOne) else 1
            right += 1


    return ''.join(newString)


word1 = "ab"
word2 = "pqrs"

print(mergeStringsAlternately(word1, word2))