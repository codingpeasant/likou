# https://leetcode.com/problems/print-zero-even-odd/description/?envType=problem-list-v2&envId=concurrency


from threading import Condition, Thread
from typing import Callable


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cond = Condition()
        self.turn = 0  # zero OR (even, odd) - 0 or 1
        self.order = 1  # order - even 0 odd 1

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: "Callable[[int], None]") -> None:
        for _ in range(self.n):
            with self.cond:
                self.cond.wait_for(lambda: self.turn == 0)
                printNumber(0)
                self.turn = (self.turn + 1) % 2
                self.cond.notify_all()

    def even(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(2, self.n + 1, 2):
            with self.cond:
                self.cond.wait_for(lambda: self.turn == 1 and self.order == 0)
                printNumber(i)
                self.order = (self.order + 1) % 2
                self.turn = (self.turn + 1) % 2
                self.cond.notify_all()

    def odd(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(1, self.n + 1, 2):
            with self.cond:
                self.cond.wait_for(lambda: self.turn == 1 and self.order == 1)
                printNumber(i)
                self.order = (self.order + 1) % 2
                self.turn = (self.turn + 1) % 2
                self.cond.notify_all()


z = ZeroEvenOdd(5)


def printNumber(n: int):
    print(n)


threadA = Thread(target=z.zero, args=(printNumber,), name="threadA")
threadB = Thread(target=z.even, args=(printNumber,), name="threadB")
threadA.start()
threadC = Thread(target=z.odd, args=(printNumber,), name="threadC")
threadB.start()
threadC.start()


threadA.join()
print("a done")
threadB.join()
print("b done")
threadC.join()
print("c done")
