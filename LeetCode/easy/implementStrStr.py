

# O(n*m); O(1)
def implementStr(haystack, needle):
    if not needle: return 0
    left, right = 0, len(needle)

    while right < len(haystack):
        if haystack[left:right] == needle:
            return left
        left, right = left + 1, right + 1

    return False, -1


# print(implementStr("hello", "ll"))


# O(n+m) || O(m) n is main string and m is the substring
def KMP(string, substring):
    haystack = string
    needle = substring
    if needle == "": return 0
    lps = [0] * len(needle)
        
    prevLPS, i = 0, 1
    while i < len(needle):
        if needle[i] == needle[prevLPS]:
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS - 1]
    
        i = 0 # ptr for haystack
        j = 0 # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1

    # if not substring: return 0
    # i, j = 0, 0
    # lps = buildPattern(substring)
    # while i < len(string):
    #     if string[i] == string[j]:
    #         i += 1
    #         j += 1
    #     else:
    #         if j == 0:
    #             i += 1
    #         else:
    #             j = lps[j-1]
        
    #     if j == len(substring):
    #         return i - len(substring)

    # return -1
    
def buildPattern(substring):
    lps = [0] * len(substring)
        
    prevLPS, i = 0, 1
    while i < len(substring):
        if substring[i] == substring[prevLPS]:
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS - 1]
    
    return lps

    # lps = [0] * len(string)

    # prevLps, i = 0, 1

    # while i < len(substring):
    #     if substring[i] == substring[prevLps]:
    #         lps[i] = prevLps + 1
    #         prevLps += 1
    #         i += 1
    #     elif prevLps == 0:
    #         lps[i] = 0
    #         i += 1
    #     else:
    #         prevLps = lps[prevLps - 1]
        
        


print(KMP('hello', 'll'))
print(KMP('a', 'a'))
