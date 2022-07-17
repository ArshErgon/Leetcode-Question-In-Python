

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


node = Node(1)
node.left = Node(2)
node.left.right = Node(5)

node.right = Node(3)
node.right.right = Node(4)


def rightSideView(node):
    if not node: return []
    stack = []
    def dfs(root, depth):
        if not root:return
        if len(stack) == depth:
            stack.append(root.value)
        dfs(root.right, depth+1)
        dfs(root.left, depth+1)

    dfs(node, 0)
    return stack


print(rightSideView(node))