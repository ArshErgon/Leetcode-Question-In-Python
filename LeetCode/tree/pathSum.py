class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




def pathSum(root, target):
    if not root:return 0

    return findSum(root, target, 0)



def findSum(root, target, total):
    if not root:
        return False

    total += root.value
    if not root.left and root.right:
        return total == target       

    return (findSum(root.left, target, total) or findSum(root.right, target, total))