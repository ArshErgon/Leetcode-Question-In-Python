
from treeNode import TreeNode as t

node = t(10)
node.left = t(5)
node.right = t(5)

# O(1) || O(1)
def rootEqualSumOfChildren(root):
    return root.value == (root.left.value + root.right.value)


print(rootEqualSumOfChildren(node))