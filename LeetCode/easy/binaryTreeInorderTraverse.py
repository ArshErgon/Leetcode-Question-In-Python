


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


node = Node(1)
node.right = Node(2)
node.right.left = Node(3)


def inorderRecursive(node, result=[]):
    if not node:
        return []
    
    inorderRecursive(node.left, result)
    result.append(node.value)
    inorderRecursive(node.right, result)

    return result


# print(inorderRecursive(node))
    



def inorderIterative(node):
    if not node:
        return []

    result, stack = [], [(node, False)]

    while stack:
        current, visited = stack.pop()
        if current:
            if visited:
                result.append(current.value)
            else:
                stack.append((current.right, False))
                stack.append((current, True))
                stack.append((current.left, False))
    
    return result

print(inorderIterative(node))