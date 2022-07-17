

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.right.left = Node(5)
node.right.right = Node(6)

def maximumWidthOfBinaryTree(tree):
    if not tree:
        return 0

    maxWidth = 1
    queue = [(tree, 1)]

    while queue:
        nextLevel = []
        for node, pos in queue:
            if node.left:
                nextLevel.append((node.left, pos * 2))
            
            if node.right:
                nextLevel.append((node.right, pos*2+1))

        if nextLevel:
            maxWidth = max(maxWidth, nextLevel[-1][1] - nextLevel[0][1] + 1)
        
        queue = nextLevel

    
    return maxWidth


print(maximumWidthOfBinaryTree(node))