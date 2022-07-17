# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        if not root:
            return 0
        return self.diameterOfTreeIlteration(root)
        
        
    def diameterOfTreeIlteration(self, node):
        if not node:
            return 0

        queue = [node] 
        height = 0

        while queue:
            size = len(queue)
            

            for _ in range(size):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                    height += 1
                if node.right:
                    queue.append(node.right)
                    height += 1

        return height 
       
    def diameterOfTreeRecursive(self, root):
        maxVal = 0
        def findLeftAndRightNode(root):
            nonlocal maxVal
            if not root:
                return -1
            
            left = findLeftAndRightNode(root.left)
            right = findLeftAndRightNode(root.right)
            
            maxVal = max(maxVal, 2 + (left + right))
            
            return max(left, right) + 1
        return maxVal
        
        findLeftAndRightNode(root)
        
        return maxVal