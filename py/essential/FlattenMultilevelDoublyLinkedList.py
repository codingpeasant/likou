# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/

from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        stored_pointers = []
        node = head
        previous_node = None

        i = 0
        while node != None or len(stored_pointers) > 0:
            if node == None:
                node = stored_pointers.pop()
                if node != None:
                    node.prev = previous_node
                continue

            if i != 0:
                previous_node.next = node
                previous_node.child = None
            previous_node = node

            if node.child != None:
                node.child.prev = node
                stored_pointers.append(node.next)
                node = node.child
            else:
                node = node.next
            i += 1

        return head
