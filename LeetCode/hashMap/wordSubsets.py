

def wordSubsets(words1, words2):
    result = []
    for i in words1:
        oldLen = len(set(i))
        aspectedLength = oldLen - len(set(words2))
        newLen = len(set(i) - set(words2))
        if newLen == aspectedLength:
            result += [i]

    return result


def wordSubsets(words1, words2):
    if not words2: return words1
    result = []
    word2Dict = {}
    for word in words2:
        word2Dict[word] = word2Dict.get(word, 0) + 1


    for word in words1:
        newDict = dict()
        for i in word:
            if i in word2Dict:
                newDict[i] = newDict.get(i, 0) + 1
        count = 0
        for key in word2Dict:
            if not key in newDict:
                break
            if newDict[key] >= word2Dict[key]:
                count += 1
        if count == len(word2Dict):
            result.append(word)


    return result

# print(wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))
# print(wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"]))
# print(wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e", "oo"]))



# O(m*n) || O(n)
def wordSubsets(word1, word2):
    if not word2:
        return word1

    result = []
    for i in word1:
        count = 0
        for j in word2:
            if j in i:
                count += 1
        if count == len(word2):
            result.append(i)
    return result


# print(wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))
# print(wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e", "oo"]))


# O(m+n) where m is words1 and nis words2
def wordSubsets(words1, words2):
    result = []
    maxCount = [0] * 26
    for word in words2:
        charFreq = getFreqOfChar(word)

        for j in range(26):
            maxCount[j] = max(maxCount[j], charFreq[j])
    
    for idx, word in enumerate(words1):
        word1CharFreq = getFreqOfChar(word)

        flag = True
        for i in range(26):
            if maxCount[i] > word1CharFreq[i]:
                flag = False
                break
        if flag:
            result.append(word)
        
    return result



def getFreqOfChar(string):
    freq = [0] * 26
    for j in string:
        freq[ord(j)-ord('a')] += 1

    return freq



print(wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))
