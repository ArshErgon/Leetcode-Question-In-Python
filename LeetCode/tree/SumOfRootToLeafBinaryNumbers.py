
from cgitb import reset
from treeNode import TreeNode as t

node = t(1)
node.left = t(1)
# node.left.right = t(1)
# node.left.left = t(0)

# node.right = t(1)
# node.right.right = t(1)
# node.right.left = t(0)


def sumOfRootToLeafBinaryNumbers(root, val=0):
    if not root: return 0
    val = val * 2 + root.value
    if not root.left and not root.right: 
        return val
    return sumOfRootToLeafBinaryNumbers(root.left, val) + sumOfRootToLeafBinaryNumbers(root.right, val)  

print(sumOfRootToLeafBinaryNumbers(node))