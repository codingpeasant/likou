# https://leetcode.com/problems/print-in-order/description/?envType=problem-list-v2&envId=concurrency

from threading import Condition, Thread
from typing import Callable


class Foo:
    def __init__(self):
        self.cond = Condition()
        self.turn = 1

    def first(self, printFirst: "Callable[[], None]") -> None:
        with self.cond:
            if self.turn == 1:
                # printFirst() outputs "first". Do not change or remove this line.
                printFirst()
                self.turn += 1
                self.cond.notify_all()

    def second(self, printSecond: "Callable[[], None]") -> None:
        with self.cond:
            self.cond.wait_for(lambda: self.turn == 2)
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.turn += 1
            self.cond.notify_all()

    def third(self, printThird: "Callable[[], None]") -> None:
        with self.cond:
            self.cond.wait_for(lambda: self.turn == 3)
            printThird()


fb = Foo()


def printFirst():
    print("first")


def printSecond():
    print("second")


def printThird():
    print("third")


threadA = Thread(target=fb.first, args=(printFirst,), name="threadA")
threadB = Thread(target=fb.second, args=(printSecond,), name="threadB")
threadA.start()
threadC = Thread(target=fb.third, args=(printThird,), name="threadC")
threadB.start()
threadC.start()

threadA.join()
threadB.join()
