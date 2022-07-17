class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n)|| O(max(n, m))

def maximumDepthOfBinaryTree(root):
    if not root: return None
    return findDepthHelper(root)



def findDepthHelper(root):
    if not root: return 0
    left = findDepthHelper(root.left)
    right = findDepthHelper(root.right)
    return max(left, right) + 1