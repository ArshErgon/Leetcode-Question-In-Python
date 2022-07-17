

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class reOrderList:
    
    def reOrder(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        
        middleNode = self.findTheMiddleNode(head)
        reverseMiddleNode = self.reverseNode(middleNode)
        
        newNode = head
        while reverseMiddleNode is not None:
            next = newNode.next
            newNode.next = reverseMiddleNode
            reverseMiddleNode = reverseMiddleNode.next
            newNode.next.next = next
            newNode = next
        
        return head

        
    def findTheMiddleNode(self, node):
        slow, fast = node, node
        
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        middle = slow.next
        slow.next = None
        return middle
    
    
    def reverseNode(self, middleNode):
        prev = None
        while middleNode is not None:
            next = middleNode.next
            middleNode.next = prev
            prev = middleNode
            middleNode = next
        
        return prev


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)
node.next.next.next.next.next = Node(6)

sol = reOrderList()
print(sol.reOrder(node))