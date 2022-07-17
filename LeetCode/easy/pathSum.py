


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


node = Node(5)
node.left = Node(4)
node.left.left = Node(11)
node.left.left.left = Node(7)
node.left.left.right = Node(2)

node.right = Node(8)
node.right.left = Node(13)
node.right.right = Node(4)
node.right.right.right = Node(1)




def pathSum(node, targetSum):
    if not node: return node
    sum_ = 0
    def helper(node, sum_):
        if not node: 
            return False

        sum_ += node.value
        if not node.left and not node.right and sum_ == targetSum:
            return  sum_ == targetSum

        return (helper(node.left, sum_) or
                helper(node.right, sum_))


    print(helper(node, sum_))

    return sum_


print(pathSum(node, 22))