



def wordBreak(string, wordDict):
    dp = [False] * (len(string) + 1)
    dp[len(string)] = True

    for i in reversed(range(len(string))):
        for w in wordDict:
            if (i+len(w)) <= len(string) and string[i:i+len(w)] == w:
                dp[i] = dp[i+len(w)]
            if dp[i]:
                break


    return dp[0]




string = "leetcode"
wordDict = ["leet", "code"]

# string = 'applepenapple'
# wordDict = ["apple","pen"]


print(wordBreak(string, wordDict))


def wordBreak(string, wordDict):
    count = len(wordDict)
    for i in range(len(string)):
        if count <= 0:
            return True
        for j in range(len(wordDict)):
            if string[i:i+len(wordDict[j])] == wordDict[j] or string[i:i+len(wordDict[j])] in wordDict:
                count -= 1
                break


    return count <= 0

# string = "leetcode"
# wordDict = ["leet", "code"]

# string = 'applepenapple'
# wordDict = ["apple","pen"]

# string = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]

string = "bb"
wordDict = ["a","b","bbb","bbbb"]


# print(wordBreak(string, wordDict))
