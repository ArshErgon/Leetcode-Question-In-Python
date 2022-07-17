class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


node = Node(5)
node.left = Node(4)
node.right = Node(6)
node.right.right = Node(7)
node.left.right = Node(3)

def searchInBinarySearchTree(root, target):
    if not root: return False

    if root.value == target:
        return root

    if root.value > target:
        return searchInBinarySearchTree(root.left, target)
    else:
        return searchInBinarySearchTree(root.right, target)
    
    return False


# print(searchInBinarySearchTree(node, 7))


def searchInBinarySearchTree(root, target):
    if not root: return root

    while root is not None:
        if root.value == target:
            return root
        elif root.value > target:
            return searchInBinarySearchTree(root.left, target) 
        else:
            return searchInBinarySearchTree(root.right, target)

    return []

print(searchInBinarySearchTree(node, 7))
