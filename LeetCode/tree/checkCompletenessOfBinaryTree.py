class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




# O(N) || O(h); where h is the height of the tree

def checkCompletenessOfBinaryTree(tree):
    if not tree: return None


def bfsHelper(tree):
    if not tree: return None
    prevNode = tree

    queue = [tree]
    while queue:
        curNode = queue.pop(0)
        if curNode:
            if not prevNode:return False
        
            queue.append(curNode.left)
            queue.append(curNode.right)
        
        prevNode = curNode
    
    return True


print(checkCompletenessOfBinaryTree())
    