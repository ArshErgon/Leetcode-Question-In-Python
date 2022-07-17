
class MyStack:

    def __init__(self):
        self.queue = []

# O(1) 
    def push(self, x: int) -> None:
        self.queue.append(x)
# O(1)
    def pop(self) -> int:
        return self.queue.pop()
# O(1)
    def top(self) -> int:
        if not self.empty():
            return self.queue[-1]
        return None

    def empty(self) -> bool:
        return len(self.queue) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())
