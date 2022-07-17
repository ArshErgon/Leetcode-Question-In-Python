
class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        if len(self.queue) > 0:
            return self.queue[-1]
        return None

    def empty(self) -> bool:
        return len(self.queue) == 0