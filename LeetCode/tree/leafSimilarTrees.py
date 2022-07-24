

from treeNode import TreeNode as t


node = t(3)
node.left = t(5)
node.right = t(1)
node.right.right = t(8)
node.right.left = t(9)
node.left.left = t(6)
node.left.right = t(2)
node.left.right.left = t(7)
node.left.right.right = t(4)



node2 = t(3)
node2.left = t(5)
node2.right = t(1)
node2.right.right = t(8)
node2.right.left = t(9)
node2.left.left = t(6)
node2.left.right = t(2)
node2.left.right.left = t(7)
node2.left.right.right = t(1)



def leafSimilarTrees(rootOne, rootTwo):
    
    if not rootOne or not rootTwo:
        return False

    return checkLeafNode(rootOne) == checkLeafNode(rootTwo)

def checkLeafNode(root):
    if not root:
        return []

    if not root.left and not root.right:
        return [root.value]
    
    return checkLeafNode(root.left) + checkLeafNode(root.right)


print(leafSimilarTrees(node, node2))