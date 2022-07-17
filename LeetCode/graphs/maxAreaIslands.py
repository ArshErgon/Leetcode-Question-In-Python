class Solution:
    def maxAreaOfIsland(self, grid):
        
        visited = [[False for row in rows]for rows in grid]
        maxIsland = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if visited[row][col]:
                    continue
                count = self.maxAreaHelper(grid, row, col, visited)
                maxIsland = max(maxIsland, count)
        return maxIsland
    
    
    def maxAreaHelper(self, grid, row, col, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or visited[row][col] or grid[row][col] == 0:
            return 0
        
        visited[row][col] = True
        
        return (1
        + self.maxAreaHelper(grid, row - 1, col, visited)
        + self.maxAreaHelper(grid, row + 1, col, visited)
        + self.maxAreaHelper(grid, row, col - 1, visited)
        + self.maxAreaHelper(grid, row, col + 1, visited)
        )
                