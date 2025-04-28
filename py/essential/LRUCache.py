# https://leetcode.com/problems/lru-cache/description/
# Grind
# Neet

from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            # if we touch a key to return its value, we need to add it
            # to the end of the least recently used items in our cache
            self.move_to_end(key)
            return self[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # check if key already exists - if yes, move item to end and update the value
        if key in self:
            self.move_to_end(key)
        # if cache is full, remove least recent item (first value in OrderedDict)
        elif len(self) == self.capacity:
            self.popitem(last=False)
        # update/add value
        self[key] = value


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache2:
    # head => node1 (old) => node2 => node3 (new/refreshed) => tail
    def __init__(self, capacity: int):
        self.dic = {}  # key to node
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoTail(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:  # similar to get()
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoTail(node)
            node.value = value  # replace the value len(dic)
        else:
            if len(self.dic) >= self.capacity:
                self.removeFromHeadAndDict()
            node = ListNode(key, value)
            self.dic[key] = node
            self.insertIntoTail(node)

    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertIntoTail(self, node):
        tailPrev = self.tail.prev
        self.tail.prev = node
        node.prev = tailPrev
        node.next = self.tail
        tailPrev.next = node

    def removeFromHeadAndDict(self):
        if len(self.dic) == 0:
            return
        headNode = self.head.next
        self.dic.pop(headNode.key)
        self.removeFromList(headNode)


s = LRUCache2(2)
s.put(1, 1)
s.put(2, 2)
s.put(3, 3)
print(s.get(1))
print(s.get(2))
print(s.get(3))
