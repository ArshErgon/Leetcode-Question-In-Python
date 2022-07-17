

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


    
class PalindromeLinkedList:
# O(n) || O(1) where n is the nuber of elements present in the
    def isPalindrome(self, node):
        slow, fast = node, node.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        middleNode = slow.next
        slow.next = None

        reversedList = self.reverseLinkedList(middleNode)

        firstHalf = node

        while reversedList is not None:
            if reversedList.value != firstHalf.value:
                return False
            reversedList = reversedList.next
            firstHalf = firstHalf.next

        return True

    
    def reverseLinkedList(self, middleNode):
        prev = None
        while middleNode is not None:
            next = middleNode.next
            middleNode.next = prev
            prev = middleNode
            middleNode = next

        return prev

        

# O(N) || O(N) where n is the number of nodes present in the linkedlist
    def palindromeLinkedListByList(self, node):
        if not node:
            return node

        stack = []

        while node is not None:
            stack.append(node.value)
            node = node.next

        left, right = 0, len(stack) - 1

        while left < right:
            if stack[left] == stack[right]:
                left += 1
                right -= 1
            else:
                return False


        return True


node = Node(1)
node.next = Node(1)
node.next.next = Node(2)
node.next.next.next = Node(1)
node.next.next.next.next = Node(1)

sol = PalindromeLinkedList()


print(sol.isPalindrome(node))
# print(sol.palindromeLinkedListByList(node))