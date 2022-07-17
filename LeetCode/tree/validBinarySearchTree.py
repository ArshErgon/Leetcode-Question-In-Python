

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def validBinarySearchTree(node):
    if not node:
        return node
    return valid(node, float('-inf'), float('inf'))


def valid(node, rootLeft, rootRight):
    if not node:
        return True

    if node.value <= rootLeft or node.value >= rootRight:
        return False

    return valid(node.left, rootLeft, node.value) and valid(node.right, node.value, rootRight)