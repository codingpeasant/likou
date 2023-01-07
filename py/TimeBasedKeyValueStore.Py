# https://leetcode.com/problems/time-based-key-value-store/
import bisect
from collections import defaultdict
from email.policy import default


class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key, value, timestamp):
        self.d[key].append([timestamp, value])

    def get(self, key, timestamp):
        v = self.d.get(key, [])
        i = bisect.bisect(
            v, [timestamp, chr(ord("z") + 1)]
        )  # needs to be larger: next element of z
        return v[i - 1][1] if i else ""


time = TimeMap()

# All the timestamps timestamp of set are strictly increasing.
time.set("foo", "bar", 1)
time.set("foo", "bar1", 2)
time.set("foo", "bar3", 4)
print(time.get("foo", 1))
print(time.get("foo", 5))
print(time.get("foo", 2))
