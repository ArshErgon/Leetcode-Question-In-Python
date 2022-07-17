
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

node = Node(3)
node.left = Node(9)
node.right = Node(20)
node.right.left = Node(15)
node.right.right = Node(7)


def sumOfLeftLeaves(root):
    if not root:return None
    sum_ = 0
    def findSum(root, isLeaf):
        if not root: return 0
        nonlocal sum_
        if isLeaf and root.left is None and root.right is None:
            sum_ += root.value
        return findSum(root.left, True) + findSum(root.right, False)        
    findSum(root.left, True)
    findSum(root.right, False)
    return sum_



print(sumOfLeftLeaves(node))