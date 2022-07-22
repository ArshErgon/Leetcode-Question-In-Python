
from treeNode import TreeNode


treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(20)
treeNode.right.left = TreeNode(15)
treeNode.right.right = TreeNode(7)


from collections import deque


# O(n) || O(d) where d is the depth of the tree
def binaryTreeLevelOrderTraversalII(root):
    if not root:
        return root

    result = []
    queue = deque([root])
    while queue:
        newLevel = []
        for _ in range(len(queue)):
            currNode = queue.popleft()
            newLevel.append(currNode.value)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

        result.append(newLevel)


    return result[::-1]


print(binaryTreeLevelOrderTraversalII(treeNode))