

def wordLadder1(beginWord, endWord, wordList):
    if not endWord in set(wordList):
        return 0
    count = 0
    beginMap = {}
    minDiff = float('inf')
    beginMap = makeDict(beginWord)

    for char in wordList:
        newDict = makeDict(char)
        diff = 0
        for key in newDict:
            if key not in beginMap:
                diff += 1
            elif beginMap[key] != newDict[key]:
                diff += 1
            
            if diff > 1:
                break

        if char == endWord:
            return count + 1

        if diff <= minDiff:
            minDiff = diff
            count += 1
            beginMap = newDict

    return count 

def makeDict(word):
    hashMap = dict()
    for char in word:
        hashMap[char] = hashMap.get(char, 0) + 1

    return hashMap


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# O(n^2*m)
from collections import defaultdict, deque
def wordLadder(beginWord, endWord, wordList):
    if not endWord in set(wordList):
        return 0

    neighbors = defaultdict(list)

    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + '*' + word[j+1:]
            neighbors[pattern].append(word)

    visited = set([beginWord]) 
    queue = deque([beginWord])
    result = 1

    while queue:
        for i in range(len(queue)):
            word = queue.popleft()
            if word == endWord:
                return result
            
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]

                for neighWord in neighbors[pattern]:
                    if neighWord not in visited:
                        visited.add(neighWord)
                        queue.append(neighWord)

        result += 1
    
    return 0
















print(wordLadder(beginWord, endWord, wordList))