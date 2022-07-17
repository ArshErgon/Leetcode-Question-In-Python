


# O(r,c) where r is row and c is col
def exists(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    seen = set()


    def searchWord(r, c, i):
        if i == len(target):
            return True
        if min(r, c) < 0 or r >= rows or c >= cols or (r, c) in seen or matrix[r][c] != target[i]:
            return False
        seen.add((r, c))

        result = (( searchWord(r + 1, c, i + 1)) or
                    searchWord(r - 1, c, i + 1) or
                    searchWord(r, c + 1, i + 1) or 
                    searchWord(r, c - 1, i + 1)
        )
        seen.remove((r, c))

        return result

    for r in range(rows):
        for c in range(cols):
            if searchWord(r, c, 0):
                return True
    return False





# print(exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED'))





def wordSearch(board, word):
    if not word:
        return True

    if not board or not board[0]:
        return False

    # visited = [[False for row in rows]for rows in board]
    visited = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (row, col) in visited:
                continue

            if searchAllDirection(row, col, board, word, visited, 0):
                return True
    return False


def searchAllDirection(row, col, board, word, visited, i):
    if i == len(word):
        return True
    if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row, col) in visited or board[row][col] != word[i]:
        return 
    print(word, board[row][col])
    
    visited.add((row, col)) 

    result = (searchAllDirection(row + 1, col, board, word, visited, i + 1) or
    searchAllDirection(row - 1, col, board, word, visited, i + 1) or 
    searchAllDirection(row, col + 1, board, word, visited, i + 1) or 
    searchAllDirection(row, col - 1, board, word, visited, i + 1) )  
    visited.remove((row, col)) 

    return result



# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

print(wordSearch(board, word))
    
