class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class ReverseNodesInKGroup:


    def reverseNodesInKGroup(self, node, k):
        dummyNode = jump = Node(0)
        dummyNode.next = l = r = node
        
        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                break

        self.printList(dummyNode.next)


    def printList(self, node):
        while node is not None:
            print(node.value, end='--->')
            node = node.next
        return None
         

   
    # def reverseNodesInKGroup(self, node, k):
    #     if not node or k == 0:
    #         return node

        
        

    # def reverseNodesInKGroupByList(self, node, n):
    #     if not node or n == 0:
    #         return node

    #     stack = []
    #     dummyNode = Node(0)

    #     tail = dummyNode

    #     n = n % self.findLength(node)
    #     newNode = node
        
    #     while newNode is not None:
    #         stack.append(newNode.value)
    #         newNode = newNode.next

    #     start = 0
    #     for i in range(n-1, len(stack), n):
    #         prev = i
    #         stack[start:i+1] = stack[start:i+1][::-1]
    #         start = prev + 1

    #     for i in stack:
    #         tail.next = Node(i)
    #         tail = tail.next
        
    #     return dummyNode.next

    # def findLength(self, n):
    #     length = 0
    #     while n is not None:
    #         length += 1
    #         n = n.next

    #     return length


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)

sol = ReverseNodesInKGroup()
print(sol.reverseNodesInKGroup(node, 2))
# print(sol.reverseNodesInKGroupByList(node, 2))