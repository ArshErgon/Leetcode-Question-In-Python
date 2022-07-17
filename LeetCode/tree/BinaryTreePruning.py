

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    
# O(N) || O(h); where h is the height of the tree

def binaryTreePruning(tree):
    if not tree: return tree
    return binaryTreeHelper(tree)



def binaryTreeHelper(tree):
    if not tree: return None

    if not tree.value and not tree.left and not tree.right:
        return None

    tree.left = binaryTreeHelper(tree.left)
    tree.right = binaryTreeHelper(tree.right)

    return tree
