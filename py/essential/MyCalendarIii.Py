# https://leetcode.com/problems/my-calendar-iii/

from sortedcontainers import SortedDict


class MyCalendarThree:
    def __init__(self):
        self.diff = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        cur = res = 0
        for delta in self.diff.values():
            cur += delta
            res = max(cur, res)
        return res


myCalendarThree = MyCalendarThree()
print(myCalendarThree.book(10, 20))
print(myCalendarThree.book(50, 60))
print(myCalendarThree.book(10, 40))
print(myCalendarThree.book(5, 15))
print(myCalendarThree.book(5, 10))
print(myCalendarThree.book(5, 100))
