
class MyCircularQueue:

    
    def __init__(self, k: int):
        self.head = self.tail = self.size = 0
        self.arr = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.arr[self.tail] = value
        self.tail = (self.tail + 1) % len(self.arr)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head + 1) % len(self.arr)
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.tail-1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.arr)


obj = MyCircularQueue(8)
print(obj.enQueue(3))
print(obj.enQueue(9))
print(obj.enQueue(5))
print(obj.enQueue(0))
print(obj.Rear())
print(obj.isFull())
print(obj.deQueue())
print(obj.Rear())

# print(obj.Front())
# print(obj.isEmpty())

["MyCircularQueue","3","9","5","0","deQueue","deQueue","isEmpty","isEmpty","Rear","Rear","deQueue"]
[[8],[3],[9],[5],[0],[],[],[],[],[],[],[]]