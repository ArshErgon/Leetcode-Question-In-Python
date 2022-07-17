



# O(n) || O(26) ===> O(1); string will only contains lowercases english characters
def maximumNumberOfBalloon(string):

    hashMap = dict()
    for i in string:
        hashMap[i] = 1 + hashMap.get(i, 0)
    
    ballonMap = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}

    minCount = float('inf')
    for key in ballonMap:
        if key not in hashMap:
            return 0
        minCount = min(minCount, hashMap[key] // ballonMap[key])
    
    return minCount



    # countText = Counter(string)
    # countBallon = Counter('ballon')

    # count = float('inf')

    # for c in countBallon:
    #     count = min(count, countText[c]//countBallon[c])
    
    # return count


print(maximumNumberOfBalloon('loonbalxballpoon'))
print(maximumNumberOfBalloon('nlaebolko'))
print(maximumNumberOfBalloon('leetcode'))
print(maximumNumberOfBalloon('lloo'))


