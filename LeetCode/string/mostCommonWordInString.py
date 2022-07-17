import re
from collections import Counter

class Solution:
    def mostCommonWord(self, string, banned):
        string = re.sub(r"[^a-zA-Z]", ' ', string).lower()
        freq = Counter(string.split())
        for x in banned:
            if x in freq:
                freq.pop(x)
            # print(dir(freq))
        # return freq.get(max(freq.values))
        return max(freq, key=freq.get)
        

sol = Solution()

print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))