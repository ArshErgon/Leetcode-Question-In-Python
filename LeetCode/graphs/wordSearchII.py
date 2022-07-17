class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end = True



def wordSearchTwo(board, words):
    if not words: return []

    root = TrieNode()
    result = set()
    for word in words:
        root.addWord(word)    
    
    rows, cols = len(board), len(board[0])

    visit = set()

    for r in range(rows):
        for c in range(cols):
            dfs(board, r, c, root, "", visit, result)

    return list(result)



def dfs(board, r, c, node, word, visit, result):
    if (r < 0 or c < 0 or r >= len(board) 
    or c >= len(board[0]) or (r, c) in visit 
    or board[r][c] not in node.children):
        return 

    visit.add((r, c))
    node = node.children[board[r][c]]
    word += board[r][c]
    if node.end:
        result.add(word)
        node.end = False
        if not node.children:
            node.children.pop(board[r][c], None)

    dfs(board, r + 1, c, node, word, visit, result)
    dfs(board, r - 1, c, node, word, visit, result)
    dfs(board, r, c + 1, node, word, visit, result)
    dfs(board, r, c - 1, node, word, visit, result)

    visit.remove((r, c))

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

print(wordSearchTwo(board, words))
