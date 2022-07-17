


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


node = Node(3)
node.left = Node(1)
node.left.right = Node(2)
node.right = Node(4)

    

def kthSmallestElement(node, k):
    if not node:
        return None

    stack = []

    def inOrder(node):
        if not node:
            return

        inOrder(node.left)
        stack.append(node.value)
        inOrder(node.right)

    inOrder(node)

    return stack[k-1]


# print(kthSmallestElement(node, 4))




