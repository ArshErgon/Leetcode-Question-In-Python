class Solution:
#     O(R,C) || O(1)
# runtime: 579ms 84.50% memory: 14.2mb 92.55%
    def islandPerimeter(self, grid):
        if not grid or not grid[0]:
            return 0
        
        perimeter = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    perimeter += 4
                
                    if row > 0 and grid[row-1][col] == 1:
                        perimeter -= 2

                    if col > 0 and grid[row][col-1] == 1:
                        perimeter -= 2
                    
        
        return perimeter


sol = Solution()
print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))