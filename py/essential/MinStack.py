# https://leetcode.com/problems/min-stack/?envType=problem-list-v2&envId=rab78cw1
# Grind


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.top())
print(obj.getMin())
