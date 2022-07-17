



def characterReplacement(string, k):
    count = {}
    res = 0
    
    l = 0
    maxf = 0
    for r in range(len(string)):
        count[string[r]] = 1 + count.get(string[r], 0)
        maxf = max(maxf, count[string[r]])
        
        if (r - l + 1) - maxf > k:
            count[string[l]] -= 1
            l += 1
        
        res = max(res, r - l + 1)
    return res



print(characterReplacement("ABBA", 2))