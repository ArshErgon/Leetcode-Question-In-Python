



def minimunWindowSubstring(string, target):
    if target == "": return ""
        
    targetHashMap, window = {}, {}
    for char in target:
        targetHashMap[char] = 1 + targetHashMap.get(char, 0)
    
    have, need = 0, len(targetHashMap)
    res, resLen = [-1, -1], float("inf")
    left = 0
    for right in range(len(string)):
        char = string[right]
        window[char] = 1 + window.get(char, 0)
        
        if char in targetHashMap and window[char] == targetHashMap[char]:
            have += 1
    
        while have == need:
            # update our result
            currentWindow = (right-left+1)
            if currentWindow < resLen:
                res = [left, right]
                resLen = currentWindow
            # pop from the left of our window
            window[string[left]] -= 1
            if string[left] in targetHashMap and window[string[left]] < targetHashMap[string[left]]:
                have -= 1
            left += 1
    left, right = res
    return string[left:right+1] if resLen != float("inf") else ""


print(minimunWindowSubstring('ADOBECODEBANC', 'ABC'))