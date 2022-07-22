class Solution:
    def rotateString(self, string: str, goal: str) -> bool:
        for i in range(len(string)):
            string = string[1:] + string[:1]
            if string == goal:
                return True
        return False

sol = Solution()

print(sol.rotateString('abcde', 'cdeab'))