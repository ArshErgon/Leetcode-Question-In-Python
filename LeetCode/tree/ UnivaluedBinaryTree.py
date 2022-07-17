
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


node = Node(1)
node.left = Node(1)
node.right = Node(1)
node.right.right = Node(1)
node.left.right = Node(1)
node.right.left = Node(1)


def univaluedBinaryTree(tree):
    if not tree:
        return None

    seen = {tree.value}
    

    # return  True if helper(tree, seen) else False
    return helper(tree, seen)

def helper(tree, seen):
    if not tree: return True
    if tree.value not in seen:
        return False

    return helper(tree.left, seen) and helper(tree.right, seen)


print(univaluedBinaryTree(node))