class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    

class PalindromeList:
    
    #   O(N) || O(1)
#   Runtime: 893ms 70.38%
    def isPalindromeIterative(self, node):
        if not node:
            return True

        slow, fast = node, node

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        middleNode = slow.next
        slow.next = None
        middleNodeReverse = self.reverseHalf(middleNode)
        newNode = node
        while middleNodeReverse is not None:
            if middleNodeReverse.val !=  newNode.val:
                return False
            middleNodeReverse = middleNodeReverse.next
            newNode = newNode.next

        return True


    def reverseHalf(self, halfNode):
        if not halfNode:
            return None
        prev = None
        while halfNode is not None:
            next = halfNode.next
            halfNode.next = prev
            prev = halfNode
            halfNode = next

        return prev
    
#     O(n) || O(n)
#     Runtime: 898ms 69.32%
    def isPalindromeByStack(self, node):
        if not node:
            return True

        stack = []

        newNode = node
        while newNode is not None:
            stack.append(newNode.val)
            newNode = newNode.next


        newNode = node
        for i in reversed(range(len(stack))):
            if stack[i] != newNode.val:
                return False
            newNode = newNode.next

        return True


node = Node(1)
node.next = Node(2)
# node.next.next = Node(1)
# node.next.next = Node(2)

sol = PalindromeList()
print(sol.isPalindromeIterative(node))
# print(sol.isPalindromeByStack(node))