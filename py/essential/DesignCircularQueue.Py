# https://leetcode.com/problems/design-circular-queue/description/
# Neet


class MyCircularQueue:
    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.q = [0] * k
        self.head = self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        if self.tail == -1:
            self.tail = self.head = 0
        else:
            self.tail = (self.tail + 1) % self.max_size
        self.q[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        if self.head == self.tail:  # last element
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.q[self.head] if self.size != 0 else -1

    def Rear(self) -> int:
        return self.q[self.tail] if self.size != 0 else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


s = MyCircularQueue(3)
print(s.enQueue(1))
print(s.enQueue(2))
print(s.enQueue(3))
print(s.enQueue(4))
print(s.Rear())
print(s.Front())
print(s.isFull())
print(s.deQueue())
print(s.deQueue())
print(s.deQueue())
print(s.deQueue())
print(s.isEmpty())
