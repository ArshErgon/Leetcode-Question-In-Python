class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    
def symmetricTree(root):
    if not root: return True
    return symmetricTreeBFS(root.right, root.left)
    return symmetricTreeHelper(root.left, root.right)


# O(n) || O(h)
def symmetricTreeHelper(root1, root2):
    if not root1 or not root2: return root1 == root2
    return (root1.value == root2.value) and symmetricTreeHelper(root1.left, root2.right) and symmetricTreeHelper(root1.right, root2.left)



def symmetricTreeBFS(root1, root2):
    if not root1 or not root2: return root1 == root2
    queue = [[root1, root2]]

    while queue:
        left, right = queue.pop(0)
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False

        if left.value != right.value:
            return False
        
        queue.append([left.left, right.right])
        queue.append([left.right, right.left])
    
    return True


node = Node(1)
node.left = Node(2)
node.left.right = Node(4)
node.left.left = Node(3)

node.right = Node(2)
node.right.left = Node(4)
node.right.right = Node(3)


print(symmetricTree(node))