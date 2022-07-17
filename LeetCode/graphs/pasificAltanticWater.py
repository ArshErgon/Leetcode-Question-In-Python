

# DFS
# O(m*n) where m is the number of cols and rows present on pasific area, and n is the number of cols and rows present on atlantic area
def waterFlow(heights):
    rows, cols = len(heights), len(heights[0])
    pasificVisited = [[False for row in rows] for rows in heights]
    altanticVisited = [[False for row in rows] for rows in heights]
    

    for col in range(cols):
        goingFourDirections(0, col, pasificVisited, heights[0][col], heights)
        goingFourDirections(rows - 1, col, altanticVisited, heights[rows - 1][col], heights)


    for row in range(rows):
        goingFourDirections(row, 0, pasificVisited, heights[row][0], heights)
        goingFourDirections(row, cols - 1, altanticVisited, heights[row][cols-1], heights)


    result = []
    for row in range(rows):
        for col in range(cols):
            if pasificVisited[row][col] and altanticVisited[row][col]:
                result.append([row, col])

    return result


def goingFourDirections(row, col, visited, prevHeight, heights):
    if row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]) or visited[row][col] or prevHeight > heights[row][col]:
        return False
    visited[row][col] = True
    print(heights[row][col], row, col)
    goingFourDirections(row + 1, col, visited, heights[row][col], heights) # down
    goingFourDirections(row - 1, col, visited, heights[row][col], heights) # up
    goingFourDirections(row, col + 1, visited, heights[row][col], heights) # right
    goingFourDirections(row, col - 1, visited, heights[row][col], heights) # left



print(waterFlow([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))



