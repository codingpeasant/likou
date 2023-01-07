# https://leetcode.com/problems/implement-queue-using-stacks/description/


class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        tempStack = []
        while self.stack:
            tempStack.append(self.stack.pop())
        self.stack.append(x)
        while tempStack:
            self.stack.append(tempStack.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return True if not self.stack else False


m = MyQueue()
m.push(1)
m.push(2)
print(m.peek())
print(m.pop())
print(m.empty())
