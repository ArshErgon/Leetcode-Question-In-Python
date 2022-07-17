



def longestPalindrome(string: str) -> str:
        if not string or len(string) < 1:
            return ''
        
        start, end = 0, 0

        for i in range(len(string)):
            odd = expandFromMiddleHelper(string, i, i)
            even = expandFromMiddleHelper(string, i, i + 1)
            maxIndex = max(odd, even)
            if maxIndex > end - start:
                start = i - ((maxIndex - 1) // 2)
                end = i + (maxIndex // 2)
                
        return string[start:end + 1]



def expandFromMiddleHelper(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1

    currentWindowSize = (right - left - 1) 
    return currentWindowSize


print(longestPalindrome('babad'))