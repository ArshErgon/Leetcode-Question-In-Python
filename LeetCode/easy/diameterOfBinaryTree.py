
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class DiameterOfBinaryTree:

    def diameterOfTreeIlterative(self, node):
        if not node:
            return 0

        queue = [node] 
        height = 0

        while queue:
            size = len(queue)
            height += 1

            for _ in range(size):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return height


    # O(N) || O(max(h))
    def diameterOfTreeRecursive(self, tree):
        if not tree:
            return 0

        maxVal = 0

        def findLeftAndRight(node):
            nonlocal maxVal
            if not node:
                return -1

            left = findLeftAndRight(node.left)
            right = findLeftAndRight(node.right)

            maxVal = max(maxVal, 2 + (left + right))

            return max(left, right) + 1
        findLeftAndRight(tree)

        return maxVal
    
tree = Node(1)
tree.right = Node(3)
tree.left = Node(2)
tree.left.left = Node(4)
tree.left.right = Node(5)


sol = DiameterOfBinaryTree()
print(sol.diameterOfTreeIlterative(tree))
# print(sol.diameterOfTreeRecursive(tree))