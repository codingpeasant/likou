# https://leetcode.com/problems/implement-stack-using-queues/description/
# Neet


class MyStack:

    def __init__(self):
      self.queue = []

    def push(self, x: int) -> None:
        tempQ = self.queue.copy()
        self.queue.clear()
        self.queue.append(x)
        self.queue.extend(tempQ)
        print(self.queue)
      

    def pop(self) -> int:
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)


    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
  
s=MyStack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())