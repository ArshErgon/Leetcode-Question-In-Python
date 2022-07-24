
from treeNode import TreeNode as t

# node = t(1)
# node.left = t(2)

node = t(5)
node.left = t(4)
node.right = t(8)
node.left.left = t(11)
node.right.right = t(4)
node.left.left.left = t(7)
node.left.left.right = t(2)
node.right.left = t(13)
node.right.right.right = t(1)
node.right.right.left = t(5)



def pathSumII(root, target):
    if not root:
        return 
    result = []
    dfs(root, 0, [], result)
    return result


def dfs(root, SUM, path, result):
    if root:
        if not root.left and not root.right and sum == root.value:
            path.append(root.value)
            result.append(path)
        dfs(root.left, sum-root.value, path+[root.value], result)
        dfs(root.right, sum-root.value, path+[root.value], result)



print(pathSumII(node, 22))