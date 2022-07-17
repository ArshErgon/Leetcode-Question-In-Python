# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head):
        pass
        # return self.partiation(head, x)
        # return self.partiationByList(head, x)

    
    
#     O(n) || O(1)

    def partiation(self, head, x):
        if not head:return head

        tmp = ans = ListNode(0)
        tmp1 = prev = ListNode(0)

        while head is not None:
            if head.val < x:
                tmp.next = head
                tmp = tmp.next

            else:
                prev.next = head
                prev = prev.next

            head = head.next

        prev.next = None
        tmp.next = tmp1.next
        return ans.next
            
# O(N) || O(N)    
    def partiationByList(self, node, x):
        if not node:
            return node

        l1, l2 = [], []
        newNode = node
        while newNode is not None:
            if newNode.val < x:
                l1.append(newNode.val)
            else:
                l2.append(newNode.val)
            newNode = newNode.next

        combineList = l1 + l2
        dummyNode = ListNode(0)
        tail = dummyNode

        for i in combineList:
            tail.next = ListNode(i)
            tail = tail.next

        return dummyNode.next