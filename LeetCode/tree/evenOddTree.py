from treeNode import TreeNode as t

node = t(1)
node.left = t(10)
node.right = t(4)
node.right.right = t(9)
node.right.right.right = t(2)
node.right.left = t(7)
node.right.left.left = t(6)
node.left.left = t(3)
node.left.left.right = t(8)
node.left.left.left = t(12)



# Runtime:838ms 44.05% || Memory: 40.8mb 57.22%
# O(n) || O(h); where h is the height of the tree
from collections import deque
def evenOddTree(root):
    if not root:
        return False
    
    level = 0
    evenOddLevel = {0:1, 1:0}
    queue = deque([root])

    while queue:
        prev = 0
        for _ in range(len(queue)):
            currNode = queue.popleft()
            comparison = {0:prev < currNode.value, 1:prev > currNode.value}
            if currNode.value % 2 != evenOddLevel[level % 2]:
                return False
            else:
                if prev != 0 and comparison[level % 2]:
                    prev = currNode.value
                elif prev == 0:
                    prev = currNode.value
                else:
                    return False

            if currNode.left:
                queue.append(currNode.left)
            
            if currNode.right:
                queue.append(currNode.right)

        level += 1

    return True


print(evenOddTree(node))