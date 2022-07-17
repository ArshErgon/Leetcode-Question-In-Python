class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



node = Node(0)
node.left = Node(3)
node.right = Node(0)


def distubuteCoinsInBinaryTree(root):
    if not root: return 0
    ans = 0

    def distubeCoins(root):
        if not root: return 0
        nonlocal ans
        left = distubeCoins(root.left)
        print(left)
        right = distubeCoins(root.right)
        print(right)
        ans += abs(left) + abs(right)
        return root.value + left + right - 1 

    
    distubeCoins(root) 
    return ans


print(distubuteCoinsInBinaryTree(node))
