

class Node:
    def __initi__(self, value):
        self.value = value
        self.left = None
        self.right = None



class MergeTwoBinaryTrees:
    # O(n +m) where n is the number of elements present in tree1; and m where m is the number of elements in tree2
    
    def mergeBinaryTrees(self, root1, root2):
        if not root1 and not root2:
            return None

        newTree = Node(root1.value + root2.value)
        newTree.left = self.mergeBinaryTrees(root1.left, root2.left)
        newTree.right = self.mergeBinaryTrees(root1.right, root2.right)

    
        return newTree



