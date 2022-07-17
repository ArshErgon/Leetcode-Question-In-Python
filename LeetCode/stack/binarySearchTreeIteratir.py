
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




class Solution:
    def __init__(self, root):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left
    

    def next(self):
        res = self.stack.pop()
        cur = cur.right

        while cur:
            self.stack.append(cur)
            cur = cur.left
        
        return res.value

    def hasNext(self):
        return len(self.stack) > 0