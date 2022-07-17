

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None



class linkedListCycle:

    #     O(N) || O(1)
    def hasCycleFastAndSlow(self, node):
        if not node:
            return node
        slow, fast = node, node.next
        while fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

#   O(n) || O(n)
    def hasCycleBySet(self, node):
        if not node:
            return False

        visited = set()

        while node is not None:
            if node in visited:
                return True
            visited.add(node)
            node = node.next

        return False
