# https://leetcode.com/problems/lfu-cache/
# Neet

from collections import defaultdict
from collections import OrderedDict


class Node:
    def __init__(self, key: int, val: int, count: int):
        self.key = key
        self.val = val
        self.count = count


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2node = defaultdict(Node)
        self.count2key2node = defaultdict(OrderedDict[Node])
        self.minCount = None  # to keep track of the global min frequency

    def get(self, key: int):
        if key not in self.key2node:
            return -1

        node: Node = self.key2node[key]
        del self.count2key2node[node.count][
            key
        ]  # remove the element first to figure out if there are any other nodes with the same count

        # clean memory if there is no node left for the count
        if not self.count2key2node[node.count]:
            del self.count2key2node[node.count]

        node.count += 1  # add frequency
        self.count2key2node[node.count][key] = node  # add it back to the end

        # if the del on line 27 have removed the whole count, it means the current Node was minCount before get - now it's increased by one and the current node count is still min
        if not self.count2key2node[self.minCount]:
            self.minCount = node.count  # or self.minCount+=1

        return node.val

    def put(self, key: int, value: int):
        if not self.cap:
            return

        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key)  # NOTICE, put makes count+1 too
            return

        if len(self.key2node) == self.cap:
            # tie - the least recently used key would be invalidated
            # If the cache is already full, we need to pop out the item with the least count.
            # If there are multiple keys with the same least count
            # we just pop out the item from the head of the OrderedDict because it's the oldest.
            k, _ = self.count2key2node[self.minCount].popitem(last=False)
            del self.key2node[k]

        self.count2key2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return


s = LFUCache(2)
s.put(1, 1)
s.put(2, 2)
s.put(3, 3)
print(s.get(1))
print(s.get(3))
print(s.get(3))
print(s.get(2))
