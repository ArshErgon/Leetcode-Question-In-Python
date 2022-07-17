

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def isSubtree(s, t):
        if not t: return True
        if not s: return False
        
        if sameTree(s, t):
            return True
        return (isSubtree(s.left, t) or
                isSubtree(s.right, t))
    
def sameTree(s, t):
    if not s and not t:
        return True
    if s and t and s.val == t.val:
        return (sameTree(s.left, t.left) and
                sameTree(s.right, t.right))
    return False