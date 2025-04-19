# https://leetcode.com/problems/time-based-key-value-store/
# Binary Search
# Grind
# Neet

import bisect
import collections


class TimeMap:
    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_right(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ""


time = TimeMap()

# All the timestamps timestamp of set are strictly increasing.
time.set("foo", "bar", 1)
time.set("foo", "bar1", 2)
time.set("foo", "bar3", 4)
print(time.get("foo", 1))
print(time.get("foo", 5))
print(time.get("foo", 2))
print(time.get("foo1", 1))
