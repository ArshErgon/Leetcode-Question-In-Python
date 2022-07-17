


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False

        i = 0
        for left in range(len(typed)):
            if i < len(name) and name[i] == typed[left]:
                i += 1
            elif left == 0 or typed[left] != typed[left-1]:
                return False

        return i == len(name)


name = "saeed"
typed = "ssaaedd"

sol = Solution()

print(sol.isLongPressedName(name, typed))
