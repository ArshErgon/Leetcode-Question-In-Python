class Solution:
    def canFinish(self, numCourses,prerequisites):
        reqMap = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            reqMap[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if reqMap[crs] == []:
                return True
            visited.add(crs)
            
            for pre in reqMap[crs]:
                if not dfs(pre):
                    return False
                
            reqMap[crs] = []
            visited.remove(crs)
                
            return True
        
        for pre in range(numCourses):
            if not dfs(pre):
                return False
            
        return True


numCourses = 2
prerequisites = [[1,0],[0,1]]

print(Solution().canFinish(numCourses, prerequisites))