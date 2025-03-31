# https://leetcode.com/problems/min-stack/?envType=problem-list-v2&envId=rab78cw1
# Grind
# Neet


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = (
            []
        )  # we need a same stack data structure that supports the stack operations and also maintains the minimum value at each index of the stack.
        # stack 1,-1,2,3,-5,5
        # minStack 1,-1,-1,-1,-5,-5

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
