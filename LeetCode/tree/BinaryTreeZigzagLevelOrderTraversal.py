
from treeNode import TreeNode


treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(20)
treeNode.right.left = TreeNode(15)
treeNode.right.right = TreeNode(7)


from collections import deque

# O(n) || O(d)
def zigZagLevelOrder(root):
    if not root:
        return root

    result = []
    queue = deque([root])
    depth = 0
    while queue:
        newLevel = []
        for _ in range(len(queue)):
            currNode = queue.popleft()
            newLevel.append(currNode.value)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

        result += [newLevel] if depth % 2 == 0 else [newLevel[::-1]]
        depth += 1

    return result

print(zigZagLevelOrder(treeNode))