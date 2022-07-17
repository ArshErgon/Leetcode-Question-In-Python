from typing import *
# O(wh)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0
        visited = [[False for col in rows] for rows in grid]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if visited[row][col]:
                    continue
                    
                sizes = self.searchDeepInGrid(grid, row, col, visited)
                if sizes > 0:
                    numOfIslands += 1
            
        return numOfIslands
                
    
    def searchDeepInGrid(self, grid, row, col, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or visited[row][col] or grid[row][col] == '0':
            return 0
        
        visited[row][col] = True
        
        return (1 
               + self.searchDeepInGrid(grid, row + 1, col, visited)
               + self.searchDeepInGrid(grid, row - 1, col, visited)
               + self.searchDeepInGrid(grid, row, col - 1, visited)
               + self.searchDeepInGrid(grid, row, col + 1, visited)
               )