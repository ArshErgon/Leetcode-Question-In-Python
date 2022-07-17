class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
# O(n) O(1)
# O(n) O(n)
# O(n) O(n)


class RemoveLinkedListElements:


    def removeElementsByIteration(self, node, ele):
        if not node:
            return node
        dummyNode = Node(-1)
        dummyNode.next = node

        prev = dummyNode
        current = node
        
        while current is not None:
            if current.value == ele:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return node

    
    def removeElementsByStack(self, node, ele):
        if not node:
            return node

        dummyNode = Node(0)
        front = dummyNode
        stack = []
        
        while node is not None:
            if node.value != ele:
                stack.append(node.value)
            node = node.next

        for val in stack:
            front.next = Node(val)
            front = front.next

        newNode = dummyNode.next

        while newNode is not None:
            print(newNode.value, end='-->')
            newNode = newNode.next


    def removeElementsByRecursion(self, node, ele):
        if not node:
            return node

        node.next = self.removeElementsByRecursion(node.next, ele)

        if node.value == ele:
            return node.next

        return node



node = Node(7)
node.next = Node(7)
node.next.next = Node(7)
node.next.next.next = Node(7)
node.next.next.next.next = Node(7)

sol = RemoveLinkedListElements()
# print(sol.removeElementsByStack(node, 2))
# x = (sol.removeElementsByRecursion(node, 2))
x = sol.removeElementsByIteration(node, 7)
while x is not None:
    print(x.value, end='-->')
    x = x.next
print()
        

