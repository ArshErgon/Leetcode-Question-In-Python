

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

node = Node(1)
node.left = Node(3)
node.right = Node(2)
node.right.right = Node(9)

node.left.left = Node(5)
node.left.right = Node(3)



# O(N) || O(h); where h is the height of the tree

def findLargestValueinEachTreeRow(tree):
    if not tree: return tree
    queue = [tree]
    result = []
    while queue:
        maximumNumber = float('-inf')
        for i in range(len(queue)):
            node = queue.pop(0)
            maximumNumber = max(maximumNumber, node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(maximumNumber)
    
    return result


print(findLargestValueinEachTreeRow(node))