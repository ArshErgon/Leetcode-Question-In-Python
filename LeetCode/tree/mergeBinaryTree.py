class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None





def mergeTwoBinaryTree(node1, node2):
    if node1 and node2:

        root = Node(node1.value + node2.value)
        root.left = mergeTwoBinaryTree(node1.left, node2.left)
        root.right = mergeTwoBinaryTree(node1.right, node2.right)
        return root
    else:
        return node1 or node2




