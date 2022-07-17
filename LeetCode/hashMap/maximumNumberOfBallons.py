

class Solution:
    def maxNumberOfBalloons(self, string: str) -> int:
        # O(n) || O(26) ===> O(1); string will only contains lowercases english characters
#         55ms 28.70%
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


text = "loonbalxballpoon"

print(Solution().maxNumberOfBalloons(text))