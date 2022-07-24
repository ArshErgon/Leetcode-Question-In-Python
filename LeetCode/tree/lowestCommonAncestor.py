
from treeNode import TreeNode as t

node = t(3)
node.left = t(5)
node.right= t(1)
node.right.right = t(8)
node.right.left = t(0)
node.left.left = t(6)
node.left.right = t(2)
node.left.right.left = t(7)
node.left.right.right = t(4)



def lowestCommonAncestor(root, p, q):
    if not root:
        return root
    
    return findAncestor(root, p, q)



def findAncestor(root, p, q):
    if not root or root.value == p or root.value == q:
        return root
    
    left = findAncestor(root.left, p, q)
    right = findAncestor(root.right, p, q)

    if not left:
        return right
    elif not right:
        return left
    else:
        return root



print(lowestCommonAncestor(node, 5, 1))