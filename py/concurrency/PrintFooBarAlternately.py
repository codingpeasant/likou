# https://leetcode.com/problems/print-foobar-alternately/description/?envType=problem-list-v2&envId=concurrency

import threading
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.cond = threading.Condition()
        self.toPrintFoo = True

    def foo(self, printFoo: "Callable[[], None]") -> None:
        for i in range(self.n):
            with self.cond:
                while not self.toPrintFoo:
                    self.cond.wait()
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.toPrintFoo = not self.toPrintFoo
                self.cond.notify_all()

    def bar(self, printBar: "Callable[[], None]") -> None:
        for i in range(self.n):
            with self.cond:
                while self.toPrintFoo:
                    self.cond.wait()
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.toPrintFoo = not self.toPrintFoo
                self.cond.notify_all()


fb = FooBar(5)


def printFoo():
    print("foo")


def printBar():
    print("bar")


threadA = threading.Thread(target=fb.foo, args=(printFoo,), name="threadA")
threadB = threading.Thread(target=fb.bar, args=(printBar,), name="threadB")
threadA.start()
threadB.start()

threadA.join()
threadB.join()
