# https://leetcode.com/problems/odd-even-linked-list/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from list_node import *


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            odd, even, evenHead = head, head.next, head.next
            while even and even.next:
                odd.next = odd.next.next
                even.next = even.next.next
                odd = odd.next
                even = even.next
            odd.next = evenHead
        return head


s = Solution()
printLinkedList(s.oddEvenList(getSampleLinkedList()))
