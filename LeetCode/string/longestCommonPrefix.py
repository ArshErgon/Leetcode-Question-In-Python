



def longestCommonPrefix(strs):
    if not strs:
            return ""
    shortest = min(strs,key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest

strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))