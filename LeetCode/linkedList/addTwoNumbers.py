# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        return self.addTwoNum(l1, l2)
        # return self.addTwoNumByList(l1, l2)
    
    def addTwoNum(self, node1, node2):
        if not node1 or not node2:
            return node1 or node2

        dummyNode = ListNode(0)
        tail = dummyNode

        carry = 0

        while node1 is not None or node2 is not None:
            v1 = node1.val if node1 is not None else 0
            v2 = node2.val if node2 is not None else 0
            SUM = v1 + v2 + carry

            tail.next = ListNode(SUM % 10)
            carry = SUM // 10
            tail = tail.next
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
        
        return dummyNode.next



    def addTwoNumByList(self, node1, node2):
        if not node1 or not node2:
            return node1 or node2

        num1, num2 = [], []

        while node1 is not None:
            num1.append(node1.val)
            node1 = node1.next

        while node2 is not None:
            num2.append(node2.val)
            node2 = node2.next


        num1, num2 = ''.join(map(str, num1[::-1])), ''.join(map(str, num2[::-1]))

        SUM = int(num1) + int(num2)

        num3 = str(SUM)[::-1]

        dummyNode = ListNode(0)
        tail = dummyNode

        for i in num3:
            tail.next = ListNode(int(i))
            tail = tail.next

        return dummyNode.next