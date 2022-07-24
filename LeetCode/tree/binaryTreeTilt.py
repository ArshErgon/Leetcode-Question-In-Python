

from treeNode import TreeNode as t

node = t(1)
node.left = t(2)
node.right = t(3)



def binaryTreeTilt(root):
    if not root:
        return 0
    res = 0
    def findTilt(root):
        nonlocal res
        if not root:
            return 0

        left = findTilt(root.left)
        right = findTilt(root.right)
        res += abs(left - right)

        return (root.value + left + right)
    findTilt(root)
    
    return res


print(binaryTreeTilt(node))