# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # return self.reverseListByList(head, left, right)
        return self.reverseList(head, left, right)

    #     O(N) with O(1) space
    def reverseList(self, node, left, right):
        if not node or left == right:
            return node

        dummyNode = ListNode(0, node)
        prevLeft, current = dummyNode, node

        for i in range(left - 1):
            prevLeft = current
            current = current.next
            

        prev = None

        for i in range(right - left + 1):
            tmp = current.next
            current.next = prev
            prev, current = current, tmp

        prevLeft.next.next = current
        prevLeft.next = prev

        return dummyNode.next
    
    # O(N) || O(n)
    def reverseListByList(self, node, left, right):
        if not node or left == right:
            return node

        stack = []
        dummyNode = ListNode(0)
        tail = dummyNode

        while node is not None:
            stack.append(node.val)
            node = node.next

        newStack = stack[:left-1] + stack[left-1:right][::-1] + stack[right:]

        for i in newStack:
            tail.next = ListNode(i)
            tail = tail.next

        return dummyNode.next