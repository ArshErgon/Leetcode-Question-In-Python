

from typing import List

class Solution:
#     O(n+m) || O(n), where n is the letter present in the word, 
# and m is the number of patterns present in the patterns
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 for letter in patterns if letter in word)