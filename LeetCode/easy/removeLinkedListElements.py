# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head, val) :
        # return self.removeElementsByIteration(head, val)
        # return self.removeElementsByStack(head, val)
        return self.removeElementsByRecursion(head, val)

    # O(N) || O(1)
    # Runtime: 88ms 54.24%
    def removeElementsByIteration(self, node, ele):
        if not node:
            return node
        dummyNode = ListNode(next=node)

        prev = dummyNode
        current = node
        
        while current is not None:
            cur = current.next
            if current.val == ele:
                prev.next = cur
            else:
                prev = current
            current = cur
            
        return dummyNode.next

    # O(N) || O(N)
    # Runtime: 82ms 63.25%
    def removeElementsByStack(self, node, ele):
        if not node:
            return node

        dummyNode = ListNode(0)
        front = dummyNode
        stack = []
        
        while node is not None:
            if node.val != ele:
                stack.append(node.val)
            node = node.next

        for val in stack:
            front.next = ListNode(val)
            front = front.next

        newNode = dummyNode.next

        return newNode

    # O(N) || O(N)
    # Runtime:85ms 58.46%
    def removeElementsByRecursion(self, node, ele):
        if not node:
            return node

        node.next = self.removeElementsByRecursion(node.next, ele)

        if node.val == ele:
            return node.next

        return node