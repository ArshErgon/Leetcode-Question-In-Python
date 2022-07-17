

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



node = Node(3)
node.left = Node(1)
node.right = Node(2)


node1 = Node(4)
node1.left = Node(9)
node1.left.left = Node(5)
node1.left.right = Node(1)
node1.right = Node(0)


def sumRootToLeaf(root):
    if not root:
        return 0

    total = 0

    def DFS(root, path):
        if not root:
            return
        nonlocal total
        if not root.left and not root.right:
            path = path*10 + root.value
            total += path

        DFS(root.left, path*10 + root.value)
        DFS(root.right, path*10 + root.value)

    DFS(root, 0)
    return total

# print(sumRootToLeaf(node))
print(sumRootToLeaf(node1))