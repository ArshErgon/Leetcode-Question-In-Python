from typing import *

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        reqMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            reqMap[crs].append(pre)

        visited = set()
        result = []
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            
            for pre in reqMap[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            result.append(crs)

            return True
        
        for pre in range(numCourses):
            if not dfs(pre):
                return []
            

        return result
        
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

print(Solution().findOrder(numCourses, prerequisites))