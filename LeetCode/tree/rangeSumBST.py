
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



node = Node(10)
node.left = Node(5)
node.left.right = Node(7)
node.left.left = Node(3)

node.right = Node(15)
node.right.right = Node(18)


def rangeSumBST(tree, low, high):
    if not tree:
        return 0
    if tree.value < low:
        return rangeSumBST(tree.right, low, high)
    if tree.value > high:
        return rangeSumBST(tree.left, low, high)
    return tree.value + rangeSumBST(tree.left, low, high) + rangeSumBST(tree.right, low, high)


print(rangeSumBST(node, 7, 15))

