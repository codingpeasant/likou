# https://leetcode.com/problems/print-foobar-alternately/description/?envType=problem-list-v2&envId=concurrency

import threading
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lockFoo = threading.Lock()
        self.lockBar = threading.Lock()
        self.lockBar.acquire()

    def foo(self, printFoo: "Callable[[], None]") -> None:
        for i in range(self.n):
            with self.lockFoo:
                printFoo()
                self.lockBar.release()
            self.lockFoo.acquire()

    def bar(self, printBar: "Callable[[], None]") -> None:
        for i in range(self.n):
            with self.lockBar:
                printBar()
                self.lockFoo.release()
            self.lockBar.acquire()


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
