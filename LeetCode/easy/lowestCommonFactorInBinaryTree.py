class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(logN) || O(1)
def lowestCommonAncestor(root, p, q):
    current = root

    while current is not None:
        if p > current.value and q > current.value:
            current = current.right
        elif current.value > p and current.value > q:
            current = current.left
        else:
            return current

    

node = Node(6)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(0)
node.left.right = Node(4)
node.left.right.left = Node(3)
node.left.right.right = Node(5)
node.right.left = Node(7)
node.right.right = Node(9)


print(lowestCommonAncestor(node, 2, 4).value)