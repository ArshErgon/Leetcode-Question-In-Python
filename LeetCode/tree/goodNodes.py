


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



node = Node(3)
node.left = Node(1)
node.left.left = Node(3)

node.right = Node(4)
node.right.left = Node(1)
node.right.right = Node(5)





def goodNodes(node):
    if not node:
        return node
    goodNode = 0

    def DFS(node, maxVal):
        if not node:
            return 
        nonlocal goodNode
        if node.value >= maxVal:
            maxVal = node.value
            goodNode += 1
        
        DFS(node.left, maxVal), DFS(node.right, maxVal)

        return goodNode
        
    DFS(node, float('-inf'))

    return goodNode


print(goodNodes(node))