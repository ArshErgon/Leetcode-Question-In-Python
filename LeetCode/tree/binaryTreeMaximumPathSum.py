

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(-10)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)




def maximumPathSum(root):
    res = [root.value]
        
    def dfs(root):
        if not root:
            return 0
        
        leftMax = dfs(root.left)
        print(leftMax)
        rightMax = dfs(root.right)
        print(rightMax, leftMax)
        
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)
        
        res[0] = max(res[0], root.value + leftMax + rightMax)
        
        return root.value + max(leftMax, rightMax)
    
    dfs(root)
    return res[0]

print(maximumPathSum(root))






