SECRET_CODE = {
    '1': '',
    '0': '',
    '2':['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

class Solution:
    def letterCombinations(self, digits):
        if digits == "":
            return []
        combination = [0] * len(digits)
        result = []
        
        self.convertDigitToSecretWord(0, digits, combination, result)
        
        return result
        
    def convertDigitToSecretWord(self, idx, digits, combination, result):
        if idx == len(digits):
            result.append(''.join(combination))
        else:
            digit = digits[idx]
            letters = SECRET_CODE[digit]
            for letter in letters:
                combination[idx] = letter
                self.convertDigitToSecretWord(idx + 1, digits, combination, result)


sol = Solution()
print(sol.letterCombinations("23"))