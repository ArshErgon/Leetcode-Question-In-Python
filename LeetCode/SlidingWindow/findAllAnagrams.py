



def findAllAnagrams(string, pattern):
    patternMap = [0] * 26
    stringMap = [0] * 26
    
    for ch in pattern:
        patternMap[ord(ch)-ord('a')] += 1
        
    left = 0
    res = list()
    for right in range(len(string)):
        stringMap[ord(string[right])-ord('a')] += 1
        if (right - left + 1) == len(pattern):
            if stringMap == patternMap:
                res.append(left)
            stringMap[ord(string[left])-ord('a')] -= 1
            
            left += 1
                
    return res


print(findAllAnagrams('cbaebabacd', 'abc'))



def findAllAnagrams(string, pattern):
    patternSet = sorted(pattern)

    result = []

    for i in range(len(string)-len(pattern)+1):
        checkAnagramString = sorted(string[i:i+len(pattern)])
        # print(checkAnagramString)
        if checkAnagramString == patternSet:
            result.append(i)
        
    return result

"ababababab"
"aab"
# print(findAllAnagrams('cbaebabacd', 'abc'))
# print(findAllAnagrams('ababababab', 'aab'))
