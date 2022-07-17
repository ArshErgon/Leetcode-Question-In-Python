from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteriod in asteroids:

            while stack and asteriod < 0 < stack[-1]:
                diff = asteriod + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    asteriod = 0
                else:
                    asteriod = 0
                    stack.pop()
            if asteriod != 0:
                stack.append(asteriod)
        return stack


print(Solution().asteroidCollision([5,10,-5]))