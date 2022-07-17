



def numberOfIslands(islands):
    if not islands: return 0

    visited = [[False for row in rows] for rows in islands]
    count = 0
    for r in range(len(islands)):
        for c in range(len(islands[r])):
            if visited[r][c]:
                continue
        
            if findIslands(r, c, islands, visited):
                count += 1


    return count



def findIslands(row, col, islands, visited):
    if row < 0 or row >= len(islands) or col < 0 or col >= len(islands[row]) or visited[row][col] or islands[row][col] != '1':
        return 0


    visited[row][col] = True

    return  (findIslands(row-1, col, islands, visited),
    findIslands(row+1, col, islands, visited),
    findIslands(row, col-1, islands, visited),
    findIslands(row, col+1, islands, visited))



# print(numberOfIslands([
#     ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]]
# ))





def numberOfIslandsBFS(islands):
    if not islands: return 0

    visited = [[False for row in rows] for rows in islands]
    count = 0

    for r in range(len(islands)):
        for c in range(len(islands[r])):
            if visited[r][c]:
                continue        
            count += findIslandsBSF(r, c, islands, visited)

    return count


def findIslandsBSF(row, col, islands, visited):
    queue = []
    count = 0
    visited[row][col] = True
    queue.append((row, col))
    while queue:
        row, col = queue.pop(0)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r, c in directions:
            if row + r < 0 or row + r >= len(islands) or col + c < 0 or col + c >= len(islands[row + r]):
                continue
            if visited[row + r][col + c]:
                continue
            if islands[row + r][col + c] == '1':
                visited[row + r][col + c] = True
                queue.append((row + r, col + c))
                count += 1

    return count

            


print(numberOfIslandsBFS([
    ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]
))