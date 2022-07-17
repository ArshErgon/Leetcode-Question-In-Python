


def longestRepeatingCharacter(string, k):
    hashMap = {}
    j = 0
    maxFreq = float('-inf')
    result = 0
    for idx, val in enumerate(string):
        hashMap[val] = hashMap.get(val, 0) + 1

        maxFreq = max(maxFreq, hashMap[val])

        if (idx - j + 1) - maxFreq > k:
            hashMap[string[j]] -= 1
            j += 1
        
        result = max(result, (idx - j + 1))


    return result



print(longestRepeatingCharacter("AABABBA", 1))