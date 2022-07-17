


def findWordsThatCanBeFormedByCharacters(words, chars):
    if not words: return None
    if not chars: return None

    charsFreq = makeFreq(chars)
    result = 0
    for word in words:
        tempFreq = charsFreq
        wordFreq = makeFreq(word)
        count = len(word)
        
        for i in range(26):
            if tempFreq[i] - wordFreq[i] < 0:
                break
            if tempFreq[i] > 0 and wordFreq[i] > 0 and tempFreq[i] >= wordFreq[i]:
                tempFreq[i] -= wordFreq[i]
                count -= 1
        if count == 0:
            result += len(word)


    return result


def makeFreq(word):
    freq = [0] * 26
    for char in word:
        freq[ord(char) - ord('a')] += 1
    return freq 

print(findWordsThatCanBeFormedByCharacters(["cat","bt","hat","tree"], "atach"))
# print(findWordsThatCanBeFormedByCharacters(["hello","world","leetcode"], 'welldonehoneyr'))