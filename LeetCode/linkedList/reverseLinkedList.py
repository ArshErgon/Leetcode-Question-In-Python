# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        return self.reverseWithStack(head)          
        # return self.iterativeReverse(head)
        # return self.recursiveReverse(head)
            
    # O(N) || O(1)
    # Runtime: 45ms 61.29%
    def iterativeReverse(self, head):
        if not head:
            return head
        
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
            
        return prev
    
    # O(N) || O(N)
    # Runtime: 50ms 47.81%
    def recursiveReverse(self, head):
        if not head:
            return head
        if not head.next:
            return head
        
        newHead = self.recursiveReverse(head.next)
        head.next.next = head
        head.next = None
        
        return newHead
    
    # O(N) || O(N)
    # Runtime: 33ms 94.92%    
    def reverseWithStack(self, head):
        if not head:
            return head
        
        stack = []
        newHead = head
        while newHead is not None:
            stack.append(newHead.val)
            newHead = newHead.next
            
        newHead = head
        
        for i in range(len(stack)):
            newHead.val = stack.pop()
            newHead = newHead.next
        return head