# https://leetcode.com/problems/lru-cache/description/

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

    def __init__(self, capacity: int):
        self.dic = dict() # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:             # similar to get()        
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value         # replace the value len(dic)
        else: 
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key,value)
            self.dic[key] = node
            self.insertIntoHead(node)
			
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertIntoHead(self, node):
        headNext = self.head.next 
        self.head.next = node 
        node.prev = self.head 
        node.next = headNext 
        headNext.prev = node
    
    def removeFromTail(self):
        if len(self.dic) == 0: return
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)
    
s = LRUCache(2)
s.put(1, 1)
s.put(2, 2)
s.put(3, 3)
print(s.get(1))
print(s.get(2))
print(s.get(3))