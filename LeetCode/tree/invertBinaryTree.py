

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    

def invertBinaryTree(root):
    if not root:
        return 

    left = invertBinaryTree(root.left)
    right = invertBinaryTree(root.right)

    root.left, root.right = left, right


    return root


