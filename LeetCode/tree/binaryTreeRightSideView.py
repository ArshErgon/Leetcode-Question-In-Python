
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.right.right = Node(4)
node.left.left = Node(5)
node.left.left.left = Node(10)


# O(N) || O(h); where h is the height of the tree

def binaryTreeRightSideView(root):
    if not root: return root
    result = []
    def helper(root, depth):
        if not root:
            return None
        if len(result) == depth:
            result.append(root.value)
        helper(root.right, depth+1)
        helper(root.left, depth+1)
    
    helper(root, 0)

    return result


print(binaryTreeRightSideView(node))