# https://leetcode.com/problems/reverse-linked-list/description/?envType=problem-list-v2&envId=oizxjoit
# Blind

from typing import Optional
from list_node import *


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev


s = Solution()
printLinkedList(s.reverseList(getSampleLinkedList()))
