
from treeNode import TreeNode as t

root = t(1)
root.left = t(2)
root.right = t(3)
root.left.right = t(5)



def binaryTreePath(root):
    if not root:
        return root
    result = []

    dfs(root, [], result)

    return result


def dfs(root, path, result):
    if not root:
        return 

    if root and not root.left and not root.right:
        path += [root.value]
        result += ['->'.join((str(x) for x in path))]
        return
    
    dfs(root.left, path + [root.value], result)
    dfs(root.right, path + [root.value], result)
    

print(binaryTreePath(root))