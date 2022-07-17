


class ValidAnagram:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    # O(n) with O(1): here 1 because  will be only dealing with lower cases english alphabelts
    def solWithList(self):
        anagrams = [0] * 26

        for i in range(len(self.str1)):
            anagrams[ord(self.str1[i]) - ord('a')] += 1
        
        for i in range(len(self.str2)):
            anagrams[ord(self.str2[i]) - ord('a')] -= 1
            
        for i in anagrams:
            if i != 0:
                return False
        return True        

# O(nlogn) || O(N)
    def sortingStrings(self):
        return sorted(self.str1) == sorted(self.str2)

# O(N) || O(N)
    def solWithSets(self):
        return set(self.str1) == set(self.str2)

sol = ValidAnagram('a', 'ab')
print(sol.solWithList())