class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.data = [0] * k   # fixed-size array
        self.front = 0        # points to the front element
        self.rear = 0         # points to the next position of last element
        self.count = 0        # number of elements

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.k) % self.k
        self.data[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.k) % self.k
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.rear - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k