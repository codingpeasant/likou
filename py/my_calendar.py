# https://leetcode.com/problems/my-calendar-i/

from bisect import bisect_left, bisect_right


class MyCalendar:
    def __init__(self):
        self.sorted_arr = []

    def book(self, start: int, end: int) -> bool:
        index_start = bisect_right(self.sorted_arr, start)
        index_end = bisect_left(self.sorted_arr, end)

        # start and end should fall into the same interval and
        # start should not fall into an existing interval
        if index_start == index_end and index_start % 2 == 0:
            self.sorted_arr.insert(index_start, start)
            self.sorted_arr.insert(index_start + 1, end)
            return True
        return False


s = MyCalendar()
print(s.book(10, 20))
print(s.book(15, 25))
print(s.book(20, 30))
