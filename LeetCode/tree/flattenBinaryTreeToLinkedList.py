

class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


node = Node(1)
node.left = Node(2)
node.right = Node(5)
node.left.left = Node(3)
node.right.right = Node(6)

# it will work in leetcode but I can't make it work it here
def flattenBinaryTreeToLinkedList(root):
    if not root or (not root.left and not root.right):
        return root

    rootList = []
    helperForList(root, rootList)

    for i in range(len(rootList)-1):
        root.value = rootList[i]
        root.right = Node()
        root.left = None
        root = root.right

    root.value = rootList[-1]

    return root


def helperForList(root, rootList):
    if not root: return None
    rootList.append(root.value)
    helperForList(root.left, rootList)
    helperForList(root.right, rootList)


# print(flattenBinaryTreeToLinkedList(node))



def flattenBinaryTreeToLinkedList(tree):
    if not tree or (not tree.left and not tree.right):
        return tree

    
    stack = [tree]

    while stack:
        node = stack.pop()

        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)

        if stack:
            node.right = stack[0]
        node.left = None

    return tree.value


print(flattenBinaryTreeToLinkedList(node))
