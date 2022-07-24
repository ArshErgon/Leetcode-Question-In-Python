from treeNode import TreeNode as t

node = t(1)
node.left = t(2)
node.right = t(3)
node.left.left = t(4)


def convertStringFromBinaryTree(root):
    if not root:
        return
    result = []
    traverseTree(root, result)
    return ''.join(str(x) for x in result)


def traverseTree(root, res):
    if not root:
        return
    res.append(root.value)

    if not root.left and not root.right:
        return

    res.append('(')
    traverseTree(root.left, res)
    res.append(')')

    if root.right:
        res.append('(')
        traverseTree(root.right,res)
        res.append(')')
    


print(convertStringFromBinaryTree(node))