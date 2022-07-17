


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


node = Node(2)
node.left = Node(1)
node.right = Node(3)

# O(n) || O(h) where n is the number of nodes present in the tree and h is the height of the tree
def findBottomLeftTreeValue(tree):
    if not tree:
        return []
    queue = [tree]
    bottomLeftValue = 0

    while queue:
        for i in range(len(queue)):
            node = queue.pop(0)
            bottomLeftValue = node.value
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
    
    return bottomLeftValue

# print(findBottomLeftTreeValue(node))


def findBottomLeftTreeValueByDFS(node):
    if not node:
        return None

    return findBottomByDFS(node, 0, node.value, 0)



def findBottomByDFS(node, maxDepth, bottomLeftVal, depth):
    if not node:
        return None
    if depth > maxDepth:
        maxDepth = depth
        bottomLeftVal = node.value
    
    findBottomByDFS(node.left, maxDepth, bottomLeftVal, depth + 1)
    findBottomByDFS(node.right, maxDepth, bottomLeftVal, depth + 1)

    return bottomLeftVal

print(findBottomLeftTreeValueByDFS(node))