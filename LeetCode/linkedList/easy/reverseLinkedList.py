class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class ReverseLinkedList:

    def iterativeReverse(self, node):
        if not node:
            return node

        prev = None
        while node is not None:
            next = node.next
            node.next = prev
            prev = node
            node = next

        while prev is not None:
            print(prev.value)
            prev = prev.next

    def withStack(self, node):
        if not node:
            return node

        stack = []

        newNode = node
        while newNode is not None:
            stack.append(newNode.value)
            newNode = newNode.next

        newNode = node

        for i in range(len(stack)):
            newNode.value = stack.pop()
            newNode = newNode.next

        while node is not None:
            print(node.value)
            node = node.next

    
    def recursiveReverse(self, node):
        if not node:
            return node
        if not node.next:
            return node

        newNode = self.recursiveReverse(node.next) 
        node.next.next = node
        node.next = None
        
        return newNode
        
    


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)
node.next.next.next.next.next = Node(6)

sol = ReverseLinkedList()
# print(sol.iterativeReverse(node))
# print(sol.withStack(node))
print(sol.recursiveReverse(node))
