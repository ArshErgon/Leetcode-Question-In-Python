

def maxInCreaseToKeepCitySkyLine(grid):
    maxRowVal = [0] * len(grid)
    maxColVal = [0] * len(grid)
    result = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            maxRowVal[row] = max(maxRowVal[row], grid[row][col])
            maxColVal[col] = max(maxColVal[col], grid[col][row])
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            result += min(maxRowVal[row], maxColVal[col]) - grid[row][col]
            
    
    return result

print(maxInCreaseToKeepCitySkyLine([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
