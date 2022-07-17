

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class RemoveDuplicateNode:

    def removeDuplicate(self, node):
        if node is None:
            return node
        
        current = node
        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

        
        while node is not None:
            print(node.value, end='--->')
            node = node.next


    def removeDuplicateWithList(self, node):
        if not node:
            return node

        stack = [node.value]
        current = node
        while current is not None:
            if current.value == stack[-1]:
                current = current.next
            else:
                stack.append(current.value)
                current = current.next

        current = node
        print(stack)
        prev = None
        for i in stack:

            current.value = i
            prev = current
            current = current.next
        
        prev.next = None

        while node is not None:
            print(node.value, end='--->')
            node = node.next




node = Node(1)
node.next = Node(1)
node.next.next = Node(2)
node.next.next.next = Node(3)
node.next.next.next.next = Node(3)
node.next.next.next.next.next  = Node(4)


sol = RemoveDuplicateNode()
print(sol.removeDuplicateWithList(node))
print(sol.removeDuplicate(node))