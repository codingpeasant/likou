# https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=problem-list-v2&envId=plakya4j
# Neet


# Definition for a Node.
from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        oldToNew = defaultdict(Node) # like cloneGraph
        cur = head
        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            oldToNew[cur].next = oldToNew.get(cur.next) # need to use get to avoid KeyError when cur.next is None
            oldToNew[cur].random = oldToNew.get(cur.random)
            cur = cur.next
        return oldToNew[head]
# Test case
s = Solution()
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node1.random = None
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1
copied_head = s.copyRandomList(node1)
print(copied_head.val)  # Output: 7
print(copied_head.next.val)  # Output: 13
print(copied_head.next.random.val)  # Output: 7
print(copied_head.next.next.val)  # Output: 11
print(copied_head.next.next.random.val)  # Output: 1
print(copied_head.next.next.next.val)  # Output: 10
print(copied_head.next.next.next.random.val)  # Output: 11
print(copied_head.next.next.next.next.val)  # Output: 1
print(copied_head.next.next.next.next.random.val)  # Output: 7