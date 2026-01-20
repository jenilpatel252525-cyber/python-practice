class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k   # use None so clearing is explicit
        self.front = 0
        self.rear = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # delete the current front item
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
