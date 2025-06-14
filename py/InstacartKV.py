from bisect import bisect_left, bisect_right
from collections import defaultdict
import copy
from sortedcontainers import SortedDict, SortedList


class Row:
    def __init__(self, value: str, timestamp: int, ttl: int):
        self.value = value
        self.timestamp = timestamp
        self.ttl = ttl

    def __str__(self):
        return f"{self.value} - {self.timestamp} - {self.ttl}"

    def expired(self, currentT: int) -> bool:
        if not self.ttl:
            return False
        return currentT - self.timestamp > self.ttl


class KVStore:
    def __init__(self):
        self.store = SortedDict()  # key -> field -> list[Row]

    def set(self, key: str, field: str, value: str, timestamp: int, ttl: int = None):
        if not self.store.get(key):
            self.store[key] = SortedDict(
                {
                    field: SortedList(
                        [Row(value, timestamp, ttl)], key=lambda x: x.timestamp
                    )
                }
            )
        elif not self.store[key].get(field):
            self.store[key][field] = SortedList(
                [Row(value, timestamp, ttl)], key=lambda x: x.timestamp
            )

        else:
            rows = self.store[key][field]
            idx = bisect_left([row.timestamp for row in rows], timestamp)
            if idx < len(rows) and rows[idx].timestamp == timestamp:
                del rows[idx]
                rows.add(Row(value, timestamp, ttl))
            else:
                self.store[key][field].add(Row(value, timestamp, ttl))

    def get(self, key: str, field: str, timestamp: str):
        if not self.store[key] or not self.store[key][field]:
            return False
        index = bisect_right(
            [row.timestamp for row in self.store[key][field]], timestamp
        )
        return self.store[key][field][index - 1] if index - 1 >= 0 else False

    def delete(self, key: str, field: str, timestamp: int):
        if not self.store[key] or not self.store[key][field]:
            return False
        index = bisect_right(
            [row.timestamp for row in self.store[key][field]], timestamp
        )
        if index - 1 >= 0:
            return self.store[key][field].pop(index - 1)
        else:
            return False


class KVStore1:
    def __init__(self):
        self.store = defaultdict(lambda: defaultdict(list))
        self.backup_data = None

    def set(self, key: str, field: str, value: str, timestamp: int, ttl: int = None):
        rows: list = self.store[key][field]
        idx = bisect_left([row.timestamp for row in rows], timestamp)
        if idx < len(rows) and rows[idx].timestamp == timestamp:
            rows[idx] = Row(value, timestamp, ttl)
        else:
            rows.insert(idx, Row(value, timestamp, ttl))

    def get(self, key: str, field: str, timestamp: int):
        rows: list = self.store[key][field]
        idx = bisect_right([row.timestamp for row in rows], timestamp)
        if idx == 0:
            return None
        row = rows[idx - 1]
        for i in range(idx - 1, -1, -1):
            if not rows[i].expired(timestamp):
                return rows[i]
        return None

    def delete(self, key: str, field: str, timestamp: int):
        rows: list = self.store[key][field]
        idx = bisect_right([row.timestamp for row in rows], timestamp)
        if idx == 0:
            return False
        return rows.pop(idx - 1)

    def getByPrefix(self, key: str, fieldPrefix: str, timestamp: int):
        res = {}
        if key in self.store:
            for field, rows in self.store[key].items():
                if field.startswith(fieldPrefix):
                    idx = bisect_right([row.timestamp for row in rows], timestamp)
                    if idx > 0:
                        row = rows[idx - 1]
                        if not row.expired(timestamp):
                            res[field] = row
        return res

    def backup(self):
        self.backup_data = copy.deepcopy(self.store)

    def restore(self):
        if self.backup_data is not None:
            self.store = copy.deepcopy(self.backup_data)


store = KVStore()
store.set("a", "b", "value1", 5)
store.set("a", "b", "value2", 10)
store.set("a", "b", "value3", 8)
store.set("a", "b", "value4", 3)
store.set("a", "b", "value5", 2)
print(store.get("a", "b", 1))
print(store.get("a", "b", 5))
print(store.get("a", "b", 9))
print(store.get("a", "b", 20))
store.set("a", "b", "value6", 2)
print(store.get("a", "b", 2))
print(store.delete("a", "b", 2))

store = KVStore1()
store.set("a", "b", "value1", 5)
store.set("a", "b", "value2", 10)
store.set("a", "b", "value3", 8)
store.set("a", "b", "value4", 3)
store.set("a", "b", "value5", 2)
print(store.get("a", "b", 1))
print(store.get("a", "b", 5))
print(store.get("a", "b", 9))
print(store.get("a", "b", 20))
store.set("a", "b", "value6", 2)
print(store.get("a", "b", 2))
print(store.delete("a", "b", 2))
store.set("a", "b1", "value51", 2, 1)  # expired
for field, row in store.getByPrefix("a", "b", 5).items():
    print(field, row)

store.backup()
store.set("a", "b2", "value52", 2, 1)
print(store.get("a", "b2", 2))  # exist
store.restore()
print(store.get("a", "b2", 2))  # none
