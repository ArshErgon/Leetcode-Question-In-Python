from treeNode import TreeNode as t

node = t(4)
node.left = t(4)
node.right = t(6)
node.left.left = t(1)
node.left.right = t(3)


def minimumabsDifferenceInBst(root):
    if not root:
        return root
    
    minVal = float('inf')
    result = []
    findMinDifference(root, result)
    
    minVal = min(minVal, min([abs(result[i] - result[i+1]) for i in range(len(result)-1)]))
    return minVal

def findMinDifference(root, res):
    if not root:
        return
    
    findMinDifference(root.left, res)
    res.append(root.value)
    findMinDifference(root.right, res)
    


print(minimumabsDifferenceInBst(node))