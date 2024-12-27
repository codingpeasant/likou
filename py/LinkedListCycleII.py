# https://leetcode.com/problems/linked-list-cycle-ii/description/

from typing import Optional
from list_node import *


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow


s = Solution()
linkedList = getSampleLinkedList()
print(s.detectCycle(linkedList))
