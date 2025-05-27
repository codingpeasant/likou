# https://leetcode.com/problems/my-calendar-i/

from bisect import bisect_left, bisect_right


class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.events:
            if not (end <= s or start >= e):
                return False
        self.events.append((start, end))
        return True


s = MyCalendar()
print(s.book(10, 20))
print(s.book(20, 30))
print(s.book(21, 23))
