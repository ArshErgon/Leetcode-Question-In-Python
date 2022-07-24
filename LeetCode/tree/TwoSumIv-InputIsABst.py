
from treeNode import TreeNode as t

node = t(5)
node.left = t(3)
node.right = t(6)
node.right.right = t(7)
node.left.left = t(2)
node.left.right = t(4)

def twoSumInputIsABST(root, target):
    if not root:
        return False
    return True if doBinarySearch(root, set(), target) else False

def doBinarySearch(root, compliment, target):
    if root:
        compli = target - root.value
        if compli in compliment:
            return True
        compliment.add(root.value)

        return doBinarySearch(root.left, compliment, target) or doBinarySearch(root.right, compliment, target)

    


print(twoSumInputIsABST(node, 9))