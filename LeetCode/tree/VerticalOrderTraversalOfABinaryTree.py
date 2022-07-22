
import queue
from treeNode import TreeNode as t

node = t(3)
node.left = t(1)
node.left.left = t(0)
node.left.right = t(2)
node.right = t(4)
node.right.left = t(2)
# node.right.right = t(7)

from collections import defaultdict, deque
def verticalOrderTraversalOfABinaryTree(root):
    if not root:
        return root

    result = []
    nodes = defaultdict(list)
    queue = deque([[root, 0, 0]])
    while queue:
        num, col, row = queue.popleft()
        nodes[col].append([row,num.value])
        
        if num.left:
            queue.append([num.left, col-1, row+1])
        if num.right:
            queue.append([num.right, col+1, row+1])
            
    for i in sorted(nodes.keys()):
        ans = [a[1] for a in sorted(nodes[i])]
        result.append(ans)
    return result


print(verticalOrderTraversalOfABinaryTree(node))