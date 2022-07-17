

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




class InvertBinaryTree:

    def invertBinaryTree(self, node):
        if not node:
            return node

        left = self.invertBinaryTree(node.left)        
        right = self.invertBinaryTree(node.right) 
        node.right = left
        node.left = right

        return self.inOrder(node)
    
    def inOrder(self, node):
        if node:
            print(node.value, end='  ')
            self.inOrder(node.left)
            self.inOrder(node.right)
        return None



node = Node(4)
node.left = Node(2)
node.left.left = Node(1)
node.left.right = Node(3)

node.right = Node(7)
node.right.right = Node(9)
node.right.left = Node(6)

sol = InvertBinaryTree()
print(sol.invertBinaryTree(node))