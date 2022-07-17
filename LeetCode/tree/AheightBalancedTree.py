class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None





node = Node(3)
node.left = Node(9)
node.right = Node(20)
node.right.left = Node(15)
node.right.right = Node(17)




def balancedBinaryTree(node):
    if not node:
        return True
    height = True
    leftHeight = getHeight(node.left)
    rightHeight = getHeight(node.right)

    if abs(leftHeight - rightHeight) > 1:
        height = False

    return height


def getHeight(node):
    if not node:
        return 0

    leftHeight = getHeight(node.left)
    rightHeight = getHeight(node.right)

    return max(leftHeight, rightHeight) + 1



print(balancedBinaryTree(node))