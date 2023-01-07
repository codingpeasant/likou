# https://leetcode.com/problems/palindrome-linked-list/

from collections import deque
from typing import Optional

from list_node import *


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_stack = deque()  # better performance than list

        p = head
        while p != None:
            node_stack.append(p.val)
            p = p.next

        p = head
        while p != None:
            value = node_stack.pop()
            if p.val != value:
                return False
            p = p.next

        return True


s = Solution()
print(s.isPalindrome(getSampleLinkedList()))
